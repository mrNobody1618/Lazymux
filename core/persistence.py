import pickle
import os

def storeFont(banner_font_style):
    # delete the pickle before storing new pickle to avoid override
    os.system("rm -rf banner.font")
    font = {'key' : banner_font_style}
    db = {}
    db['font'] = font
    dbfile = open('banner.font', 'ab')
    pickle.dump(db, dbfile)
    dbfile.close()

def loadFont():
    try:
        dbfile = open('banner.font', 'rb')
        db = pickle.load(dbfile)
        return db['font']['key']
    except IOError:
        return ''

