%module swiggimp
%{
#include <vector>
#include "defs.h"
#include "scene.h"
#include "mesh.h"
#include "Importer.hpp"
#include "postprocess.h"
%}

#define ASSIMP_API
#define AI_FORCE_INLINE

%ignore aiScene::~aiScene();
%ignore aiFace::operator=;

%include "defs.h"
%include "scene.h"
%include "mesh.h"
%include "Importer.hpp"
%include "postprocess.h"

%include "std_vector.i"
namespace std {
   %template(FloatVector) vector<float>;
}


%extend aiMesh {
  std::vector<float> vertexValues() {
    std::vector<float> values($self->mNumVertices * 3);
    for (unsigned int i=0; i < $self->mNumVertices; i++) {
      values[3*i] = $self->mVertices[i].x;
      values[3*i + 1] = $self->mVertices[i].y;
      values[3*i + 2] = $self->mVertices[i].z;
    }
    return values;
  }

  static aiMesh* valueAt(aiMesh** meshes, int i) {
    return meshes[i];
  }
};

