from collections import ChainMap

defaults = {'theme':'Default', 'language':'eng', 'showIndex':True,
            'showFooter':True }

cm = ChainMap(defaults)

cm2 = cm.new_child({'theme':'bluesky'}) # creates a new chainmap with a 
# child that overrides the parent

print(cm2['theme'])

print(cm2.pop('theme'))

print(cm2['theme'])

cm2.maps[0] = {'theme':'desert', 'showIndex':False} # adds a 'root context' 

print(cm2['showIndex'])

print(cm2)

print(cm2.parents)