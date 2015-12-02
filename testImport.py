import swiggimp

importer = swiggimp.Importer()
scene = importer.ReadFile("Dragon.dae", 0)
mesh = swiggimp.aiMesh.valueAt(scene.mMeshes, 0)
verVal = mesh.vertexValues()
print(verVal[0])
print(verVal[verVal.size() - 1])

