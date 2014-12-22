namespace java ca.mcpnet.isoblockprojector

struct IBPdVector {
    1:required double x;
    2:required double y;
    3:required double z;
}

struct IBPiVector {
    1:required i32 x;
    2:required i32 y;
    3:required i32 z;
}

struct IBPPlayer {
    1:required i32 id;
    2:required string name;
    3:required i32 worldid;
    4:required IBPdVector location;
}

struct IBPProjectionFrame {
    1:required IBPiVector size;
    2:required binary blockdata;
}

typedef list<IBPPlayer> PlayerList

service IsoBlockProjectorService
{
    string getVersion()

    PlayerList getPlayerList()

    IBPProjectionFrame getDownFrame(1:i32 worldid 2:IBPiVector location, 3:IBPiVector size)
}
