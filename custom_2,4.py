from mininet.topo import Topo

class MyTopo( Topo ):
    "2 host, 4 switch"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        s1 = self.addSwitch( 's1' )
	s2 = self.addSwitch( 's2' )

	s3 = self.addSwitch( 's_12' )
        s4 = self.addSwitch( 's_21' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s2 )

	self.addLink( s1, s3 )
	self.addLink( s3, s2 )

	self.addLink( s1, s4 )
	self.addLink( s4, s2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
