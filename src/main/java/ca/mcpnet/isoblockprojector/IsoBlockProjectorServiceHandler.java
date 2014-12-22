package ca.mcpnet.isoblockprojector;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.server.MinecraftServer;
import net.minecraft.world.WorldServer;

import org.apache.thrift.TException;

public class IsoBlockProjectorServiceHandler implements IsoBlockProjectorService.Iface {

	@Override
	public String getVersion() throws TException {
		return IsoBlockProjector.VERSION;
	}

	@Override
	public List<IBPPlayer> getPlayerList() throws TException {
		List<IBPPlayer> list = new ArrayList<IBPPlayer>();
        // Lets get a list of worlds
		for (int i = 0; i < MinecraftServer.getServer().worldServers.length; i++) {
			WorldServer world = MinecraftServer.getServer().worldServers[i];
			// Get the players
			Iterator pitr = world.playerEntities.iterator();
			while (pitr.hasNext()) {
				EntityPlayer player = (EntityPlayer) pitr.next();
				list.add(new IBPPlayer(player.getEntityId(),
						player.getDisplayName(),
						world.provider.dimensionId,
						new IBPdVector(player.posX,player.posY,player.posZ)));
			}
		}
		
		return list;
	}

	@Override
	public IBPProjectionFrame getDownFrame(int worldid, IBPiVector location,
			IBPiVector size) throws TException {
		throw new TException("endpoint unimplemented");
	}

}
