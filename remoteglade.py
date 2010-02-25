#!/usr/bin/python -i
# vim: set fileencoding=utf-8

import pygtk
pygtk.require( "2.0" )
import gtk

import remotecontrol

class Remote:
    def gtk_main_quit( self, window ):
        gtk.main_quit()

    def searchchanged(self, window):
        value = 'Nina' #FIXME
        self.reset_search()
        artists = self.remote.searchartist(value)
        self.add_results("Artists", artists)
        albums = self.remote.searchalbum(value)
        self.add_results("Albums", albums)
        tracks = self.remote.searchtracks(value)
        self.add_results("Tracks", tracks)
        
    def reset_search(self):
        print "Reset search"   
        
    def add_results(self, category, results):
        #FIXME
        print category, results
        
        
    def volumerelease(self, window):
        volume = 50  #FIXME
        self.remote.volume(volume)
        self.update_volume()
    
    def update_volume()
        volume = self.remote.getvolume()
        #FIXME
        
    def trackseek(self, window, value):
        print "trackseek", window, value
        

    def nextitem(self, window):
        self.remote.skip()
        self.update_status()
        
    def play(self, window):
        self.remote.play()
        self.update_status()
        
    def previtem(self, window):
        self.remote.prev()
        self.update_status()

    def cb_delete_event( self, window, event ):
        # Run dialog
        response = self.quit_dialog.run()
        self.quit_dialog.hide()

        return response != 1

    def cb_show_about( self, button ):
        # Run dialog
        self.about_dialog.run()
        self.about_dialog.hide()

    def update_status(self):
        status = self.remote.showStatus()

    def init_speakers(self):
        #FIXME
        self.remote.getspeakers()

    def __init__( self ):
        builder = gtk.Builder()
        builder.add_from_file( "glade/remote.glade" )
        
        self.window       = builder.get_object( "window2" )
        self.about_dialog = builder.get_object( "aboutdialog1" )
        self.quit_dialog  = builder.get_object( "dialog1" )
        
        self.track = builder.get_object("Track")
        self.artist = builder.get_object("Artist")
        self.time = builder.get_object("time")
        self.timeremain = builder.get_object("timeremain")

        self.searchresults = builder.get_object("treestore1")
        self.speakers = builder.get_object("combobox1")

        builder.connect_signals( self )

        self.remote = remotecontrol.remote()
        self.init_speakers()
        self.update_status()

if __name__ == "__main__":
    win = Remote()
    win.window.show_all()
    gtk.main()
