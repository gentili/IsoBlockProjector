package ca.mcpnet.isoblockprojector;

import java.util.Map;

import org.apache.logging.log4j.Logger;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.server.TNonblockingServer;
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TNonblockingServerSocket;
import org.apache.thrift.transport.TNonblockingServerTransport;

import ca.mcpnet.isoblockprojector.IsoBlockProjectorService.Processor;
import net.minecraft.init.Blocks;
import net.minecraftforge.common.MinecraftForge;
import cpw.mods.fml.common.FMLCommonHandler;
import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.Mod.EventHandler;
import cpw.mods.fml.common.Mod.Instance;
import cpw.mods.fml.common.event.FMLInitializationEvent;
import cpw.mods.fml.common.event.FMLPostInitializationEvent;
import cpw.mods.fml.common.event.FMLPreInitializationEvent;
import cpw.mods.fml.common.event.FMLServerStartedEvent;
import cpw.mods.fml.common.event.FMLServerStoppingEvent;
import cpw.mods.fml.common.eventhandler.SubscribeEvent;
import cpw.mods.fml.common.gameevent.TickEvent;
import cpw.mods.fml.common.network.NetworkCheckHandler;
import cpw.mods.fml.relauncher.Side;

@Mod(modid = IsoBlockProjector.MODID, version = IsoBlockProjector.VERSION)
public class IsoBlockProjector
{
    public static final String MODID = "isoblockprojector";
    public static final String MODNAME = "Isometric Block Projector Mod";
    public static final String VERSION = "1.0";
    
    @Instance(value = IsoBlockProjector.MODID)
    public static IsoBlockProjector instance;
    
	public static Logger log;

	private Thread IBPserverthread;
	private TIsoBlockProjectorServer IBPserver;

	/*
	 * The following are Forge and FML specific methods
	 */
	@NetworkCheckHandler
	public static boolean networkCheckHandler(Map<String, String> map, Side side) {
		return true;
	}

	@EventHandler
	public void onFMLPreInitializationEvent(FMLPreInitializationEvent e) {
		log = e.getModLog();
		log.info("Logging enabled");
	}
	
	@EventHandler
	public void onFMLPostInitializationEvent(FMLPostInitializationEvent e) {
		
	}
        
    @EventHandler
    public void onFMLServerStartedEvent(FMLServerStartedEvent e) {
    	log.info("Starting BlockTransfer server on port 9090");
    	
		IsoBlockProjectorServiceHandler handler = new IsoBlockProjectorServiceHandler();
		Processor processor = new IsoBlockProjectorService.Processor(handler);

		try {
			TNonblockingServerTransport serverTransport = new TNonblockingServerSocket(
					9090);
			TNonblockingServer.Args serverArgs = new TNonblockingServer.Args(serverTransport);
			serverArgs.processor(processor);
			serverArgs.transportFactory(new TFramedTransport.Factory());
			serverArgs.protocolFactory(new TBinaryProtocol.Factory(true, true));
			IBPserver = new TIsoBlockProjectorServer(serverArgs);
			IBPserverthread = new Thread() {
				public void run() {
					IBPserver.serve();
				}
			};
			IBPserverthread.start();
		} catch (Exception ex) {
			throw new RuntimeException("Unable to start BlockTransfer server",ex);
		}
        MinecraftForge.EVENT_BUS.register(this);
        FMLCommonHandler.instance().bus().register(this);
    }
    
    @EventHandler
    public void onFMLServerStoppingEvent(FMLServerStoppingEvent e) {
    	log.info("Stopping BlockTransfer server");
    	MinecraftForge.EVENT_BUS.unregister(this);
        FMLCommonHandler.instance().bus().unregister(this);
        IBPserver.stop();
        try {
			IBPserverthread.join();
		} catch (InterruptedException ex) {
			throw new RuntimeException("Interrupted during BlockTransfer server shutdown",ex);
		}
    }
    
    @SubscribeEvent
    public void handle(TickEvent e) {
    	// Need to handle requests in the context of the main
    	// server thread as they may request info from the world
    	// or modify the world
    	if (e.type == TickEvent.Type.SERVER)
    		if (e.phase == TickEvent.Phase.START)
    			IBPserver.serviceRequestQueue();
    }
}
