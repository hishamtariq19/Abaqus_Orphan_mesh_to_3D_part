# A very simple brute force virtual topology; works very well with most of the structural engineering structures.
# Run it on trial model first.
# Optimization will be required for complex structures.
model_name = 'Model-1'   #put the name of the model of interest.
new_part_name = 'new_part' #put the name of the part created from mesh
d = 1000;        # <<<----put the value of largest dimension of the part (Units of length used in Abaqus)
null = d     # value of null my be varied for better results from d to 1000*d
mdb.models[model_name].parts[new_part_name]._previewCreateVirtualTopology()
mdb.models[model_name].parts[new_part_name].createVirtualTopology(
    applyBlendControls=True, blendRadiusTolerance=0.17, 
    blendSubtendedAngleTolerance=60.0, cornerAngleTolerance=30.0, 
    faceAspectRatioThreshold=null, ignoreRedundantEntities=True, 
    mergeShortEdges=True, mergeSliverFaces=True, mergeSmallAngleFaces=True, 
    mergeSmallFaces=True, mergeThinStairFaces=True, shortEdgeThreshold=null, 
    smallFaceAreaThreshold=null, smallFaceCornerAngleThreshold=null, 
    thinStairFaceThreshold=null)

