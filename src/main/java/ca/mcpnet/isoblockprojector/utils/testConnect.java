package ca.mcpnet.isoblockprojector.utils;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransportException;

import ca.mcpnet.isoblockprojector.IBPProjectionFrame;
import ca.mcpnet.isoblockprojector.IBPiVector;
import ca.mcpnet.isoblockprojector.IsoBlockProjectorService;

public final class testConnect {

	public static void main(String[] args) throws TException {
		System.out.println("Initial connect...");
		TFramedTransport transport = new TFramedTransport(new TSocket("localhost",9090));
		transport.open();
		TProtocol protocol = new TBinaryProtocol(transport);
		IsoBlockProjectorService.Client client = new IsoBlockProjectorService.Client(protocol);
		
		System.out.println("Version: "+ client.getVersion());
		
		IBPProjectionFrame frame = client.getDownFrame(0, new IBPiVector(0,0,0),new IBPiVector(0,0,0));
	}

}
