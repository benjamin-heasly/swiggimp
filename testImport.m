clear
clc

importer = py.swiggimp.Importer();
scene = importer.ReadFile('Dragon.dae', uint32(0));
mesh = py.swiggimp.aiMesh.valueAt(scene.mMeshes, uint32(0));
verVal = mesh.vertexValues();

nVals = double(verVal.size());
drMesh = zeros(3, nVals/3);
verIter = verVal.iterator();

% quite slow
for ii = 1:nVals
  drMesh(ii) = double(verIter.next());
end

scatter3(drMesh(1,:), drMesh(2,:), drMesh(3,:), '.');
