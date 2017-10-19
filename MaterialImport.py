import c4d
from c4d import gui
from random import randint
#Welcome to the world of Python

 
def main():
    #gui.MessageDialog('Hello World!')

    doc = c4d.documents.GetActiveDocument()
    materialList = doc.GetMaterials()

    for material in materialList:

        materialName = material.GetName()
        #print (materialName)

        r = randint(0, 255)
        g = randint(0, 255)
        b= randint(0, 255)

        print (r, g, b)

        layer = CreateLayer(materialName, c4d.Vector(r, g, b))

        material.SetLayerObject(layer)
        #material.InsertUnder(layer)

        #print(material.GetLayerObject())


def CreateLayer (layername, layercolor):
    
    doc = c4d.documents.GetActiveDocument()
    root = doc.GetLayerObjectRoot() #Gets the layer manager
    LayersList = root.GetChildren() #Get Layer list
    
    # check if layer already exist
    layerexist = False
    for layer in LayersList:
        name = layer.GetName()
        if (name == layername):
            return layer
        
    c4d.CallCommand(100004738) # New Layer
    c4d.EventAdd()
    
    #rename new layer
    LayersList = root.GetChildren() #redo getchildren, because a new one was added.
    
    for layer in LayersList:
        
        name = layer.GetName()
        
        if (name == "Layer"):
            layer.SetName(layername)
            layer.SetBit(c4d.BIT_ACTIVE) # set layer active
            layer[c4d.ID_LAYER_COLOR] = layercolor

            layerData = {'color': layercolor, 'solo' : False}
            layer.SetLayerData(doc, layerData)

            c4d.EventAdd()

            return layer


if __name__=='__main__':
 main()