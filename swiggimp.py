# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_swiggimp', [dirname(__file__)])
        except ImportError:
            import _swiggimp
            return _swiggimp
        if fp is not None:
            try:
                _mod = imp.load_module('_swiggimp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _swiggimp = swig_import_helper()
    del swig_import_helper
else:
    import _swiggimp
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


AI_MATH_PI = _swiggimp.AI_MATH_PI
AI_MATH_TWO_PI = _swiggimp.AI_MATH_TWO_PI
AI_MATH_HALF_PI = _swiggimp.AI_MATH_HALF_PI
AI_MATH_PI_F = _swiggimp.AI_MATH_PI_F
AI_MATH_TWO_PI_F = _swiggimp.AI_MATH_TWO_PI_F
AI_MATH_HALF_PI_F = _swiggimp.AI_MATH_HALF_PI_F
class aiNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mName"] = _swiggimp.aiNode_mName_set
    __swig_getmethods__["mName"] = _swiggimp.aiNode_mName_get
    if _newclass:mName = _swig_property(_swiggimp.aiNode_mName_get, _swiggimp.aiNode_mName_set)
    __swig_setmethods__["mTransformation"] = _swiggimp.aiNode_mTransformation_set
    __swig_getmethods__["mTransformation"] = _swiggimp.aiNode_mTransformation_get
    if _newclass:mTransformation = _swig_property(_swiggimp.aiNode_mTransformation_get, _swiggimp.aiNode_mTransformation_set)
    __swig_setmethods__["mParent"] = _swiggimp.aiNode_mParent_set
    __swig_getmethods__["mParent"] = _swiggimp.aiNode_mParent_get
    if _newclass:mParent = _swig_property(_swiggimp.aiNode_mParent_get, _swiggimp.aiNode_mParent_set)
    __swig_setmethods__["mNumChildren"] = _swiggimp.aiNode_mNumChildren_set
    __swig_getmethods__["mNumChildren"] = _swiggimp.aiNode_mNumChildren_get
    if _newclass:mNumChildren = _swig_property(_swiggimp.aiNode_mNumChildren_get, _swiggimp.aiNode_mNumChildren_set)
    __swig_setmethods__["mChildren"] = _swiggimp.aiNode_mChildren_set
    __swig_getmethods__["mChildren"] = _swiggimp.aiNode_mChildren_get
    if _newclass:mChildren = _swig_property(_swiggimp.aiNode_mChildren_get, _swiggimp.aiNode_mChildren_set)
    __swig_setmethods__["mNumMeshes"] = _swiggimp.aiNode_mNumMeshes_set
    __swig_getmethods__["mNumMeshes"] = _swiggimp.aiNode_mNumMeshes_get
    if _newclass:mNumMeshes = _swig_property(_swiggimp.aiNode_mNumMeshes_get, _swiggimp.aiNode_mNumMeshes_set)
    __swig_setmethods__["mMeshes"] = _swiggimp.aiNode_mMeshes_set
    __swig_getmethods__["mMeshes"] = _swiggimp.aiNode_mMeshes_get
    if _newclass:mMeshes = _swig_property(_swiggimp.aiNode_mMeshes_get, _swiggimp.aiNode_mMeshes_set)
    __swig_setmethods__["mMetaData"] = _swiggimp.aiNode_mMetaData_set
    __swig_getmethods__["mMetaData"] = _swiggimp.aiNode_mMetaData_get
    if _newclass:mMetaData = _swig_property(_swiggimp.aiNode_mMetaData_get, _swiggimp.aiNode_mMetaData_set)
    def __init__(self, *args): 
        this = _swiggimp.new_aiNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_aiNode
    __del__ = lambda self : None;
    def FindNode(self, *args): return _swiggimp.aiNode_FindNode(self, *args)
aiNode_swigregister = _swiggimp.aiNode_swigregister
aiNode_swigregister(aiNode)

AI_SCENE_FLAGS_INCOMPLETE = _swiggimp.AI_SCENE_FLAGS_INCOMPLETE
AI_SCENE_FLAGS_VALIDATED = _swiggimp.AI_SCENE_FLAGS_VALIDATED
AI_SCENE_FLAGS_VALIDATION_WARNING = _swiggimp.AI_SCENE_FLAGS_VALIDATION_WARNING
AI_SCENE_FLAGS_NON_VERBOSE_FORMAT = _swiggimp.AI_SCENE_FLAGS_NON_VERBOSE_FORMAT
AI_SCENE_FLAGS_TERRAIN = _swiggimp.AI_SCENE_FLAGS_TERRAIN
class aiScene(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiScene, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiScene, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mFlags"] = _swiggimp.aiScene_mFlags_set
    __swig_getmethods__["mFlags"] = _swiggimp.aiScene_mFlags_get
    if _newclass:mFlags = _swig_property(_swiggimp.aiScene_mFlags_get, _swiggimp.aiScene_mFlags_set)
    __swig_setmethods__["mRootNode"] = _swiggimp.aiScene_mRootNode_set
    __swig_getmethods__["mRootNode"] = _swiggimp.aiScene_mRootNode_get
    if _newclass:mRootNode = _swig_property(_swiggimp.aiScene_mRootNode_get, _swiggimp.aiScene_mRootNode_set)
    __swig_setmethods__["mNumMeshes"] = _swiggimp.aiScene_mNumMeshes_set
    __swig_getmethods__["mNumMeshes"] = _swiggimp.aiScene_mNumMeshes_get
    if _newclass:mNumMeshes = _swig_property(_swiggimp.aiScene_mNumMeshes_get, _swiggimp.aiScene_mNumMeshes_set)
    __swig_setmethods__["mMeshes"] = _swiggimp.aiScene_mMeshes_set
    __swig_getmethods__["mMeshes"] = _swiggimp.aiScene_mMeshes_get
    if _newclass:mMeshes = _swig_property(_swiggimp.aiScene_mMeshes_get, _swiggimp.aiScene_mMeshes_set)
    __swig_setmethods__["mNumMaterials"] = _swiggimp.aiScene_mNumMaterials_set
    __swig_getmethods__["mNumMaterials"] = _swiggimp.aiScene_mNumMaterials_get
    if _newclass:mNumMaterials = _swig_property(_swiggimp.aiScene_mNumMaterials_get, _swiggimp.aiScene_mNumMaterials_set)
    __swig_setmethods__["mMaterials"] = _swiggimp.aiScene_mMaterials_set
    __swig_getmethods__["mMaterials"] = _swiggimp.aiScene_mMaterials_get
    if _newclass:mMaterials = _swig_property(_swiggimp.aiScene_mMaterials_get, _swiggimp.aiScene_mMaterials_set)
    __swig_setmethods__["mNumAnimations"] = _swiggimp.aiScene_mNumAnimations_set
    __swig_getmethods__["mNumAnimations"] = _swiggimp.aiScene_mNumAnimations_get
    if _newclass:mNumAnimations = _swig_property(_swiggimp.aiScene_mNumAnimations_get, _swiggimp.aiScene_mNumAnimations_set)
    __swig_setmethods__["mAnimations"] = _swiggimp.aiScene_mAnimations_set
    __swig_getmethods__["mAnimations"] = _swiggimp.aiScene_mAnimations_get
    if _newclass:mAnimations = _swig_property(_swiggimp.aiScene_mAnimations_get, _swiggimp.aiScene_mAnimations_set)
    __swig_setmethods__["mNumTextures"] = _swiggimp.aiScene_mNumTextures_set
    __swig_getmethods__["mNumTextures"] = _swiggimp.aiScene_mNumTextures_get
    if _newclass:mNumTextures = _swig_property(_swiggimp.aiScene_mNumTextures_get, _swiggimp.aiScene_mNumTextures_set)
    __swig_setmethods__["mTextures"] = _swiggimp.aiScene_mTextures_set
    __swig_getmethods__["mTextures"] = _swiggimp.aiScene_mTextures_get
    if _newclass:mTextures = _swig_property(_swiggimp.aiScene_mTextures_get, _swiggimp.aiScene_mTextures_set)
    __swig_setmethods__["mNumLights"] = _swiggimp.aiScene_mNumLights_set
    __swig_getmethods__["mNumLights"] = _swiggimp.aiScene_mNumLights_get
    if _newclass:mNumLights = _swig_property(_swiggimp.aiScene_mNumLights_get, _swiggimp.aiScene_mNumLights_set)
    __swig_setmethods__["mLights"] = _swiggimp.aiScene_mLights_set
    __swig_getmethods__["mLights"] = _swiggimp.aiScene_mLights_get
    if _newclass:mLights = _swig_property(_swiggimp.aiScene_mLights_get, _swiggimp.aiScene_mLights_set)
    __swig_setmethods__["mNumCameras"] = _swiggimp.aiScene_mNumCameras_set
    __swig_getmethods__["mNumCameras"] = _swiggimp.aiScene_mNumCameras_get
    if _newclass:mNumCameras = _swig_property(_swiggimp.aiScene_mNumCameras_get, _swiggimp.aiScene_mNumCameras_set)
    __swig_setmethods__["mCameras"] = _swiggimp.aiScene_mCameras_set
    __swig_getmethods__["mCameras"] = _swiggimp.aiScene_mCameras_get
    if _newclass:mCameras = _swig_property(_swiggimp.aiScene_mCameras_get, _swiggimp.aiScene_mCameras_set)
    def __init__(self): 
        this = _swiggimp.new_aiScene()
        try: self.this.append(this)
        except: self.this = this
    def HasMeshes(self): return _swiggimp.aiScene_HasMeshes(self)
    def HasMaterials(self): return _swiggimp.aiScene_HasMaterials(self)
    def HasLights(self): return _swiggimp.aiScene_HasLights(self)
    def HasTextures(self): return _swiggimp.aiScene_HasTextures(self)
    def HasCameras(self): return _swiggimp.aiScene_HasCameras(self)
    def HasAnimations(self): return _swiggimp.aiScene_HasAnimations(self)
    __swig_setmethods__["mPrivate"] = _swiggimp.aiScene_mPrivate_set
    __swig_getmethods__["mPrivate"] = _swiggimp.aiScene_mPrivate_get
    if _newclass:mPrivate = _swig_property(_swiggimp.aiScene_mPrivate_get, _swiggimp.aiScene_mPrivate_set)
aiScene_swigregister = _swiggimp.aiScene_swigregister
aiScene_swigregister(aiScene)

AI_MAX_FACE_INDICES = _swiggimp.AI_MAX_FACE_INDICES
AI_MAX_BONE_WEIGHTS = _swiggimp.AI_MAX_BONE_WEIGHTS
AI_MAX_VERTICES = _swiggimp.AI_MAX_VERTICES
AI_MAX_FACES = _swiggimp.AI_MAX_FACES
AI_MAX_NUMBER_OF_COLOR_SETS = _swiggimp.AI_MAX_NUMBER_OF_COLOR_SETS
AI_MAX_NUMBER_OF_TEXTURECOORDS = _swiggimp.AI_MAX_NUMBER_OF_TEXTURECOORDS
class aiFace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiFace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiFace, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mNumIndices"] = _swiggimp.aiFace_mNumIndices_set
    __swig_getmethods__["mNumIndices"] = _swiggimp.aiFace_mNumIndices_get
    if _newclass:mNumIndices = _swig_property(_swiggimp.aiFace_mNumIndices_get, _swiggimp.aiFace_mNumIndices_set)
    __swig_setmethods__["mIndices"] = _swiggimp.aiFace_mIndices_set
    __swig_getmethods__["mIndices"] = _swiggimp.aiFace_mIndices_get
    if _newclass:mIndices = _swig_property(_swiggimp.aiFace_mIndices_get, _swiggimp.aiFace_mIndices_set)
    __swig_destroy__ = _swiggimp.delete_aiFace
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _swiggimp.new_aiFace(*args)
        try: self.this.append(this)
        except: self.this = this
    def __eq__(self, *args): return _swiggimp.aiFace___eq__(self, *args)
    def __ne__(self, *args): return _swiggimp.aiFace___ne__(self, *args)
aiFace_swigregister = _swiggimp.aiFace_swigregister
aiFace_swigregister(aiFace)

class aiVertexWeight(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiVertexWeight, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiVertexWeight, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mVertexId"] = _swiggimp.aiVertexWeight_mVertexId_set
    __swig_getmethods__["mVertexId"] = _swiggimp.aiVertexWeight_mVertexId_get
    if _newclass:mVertexId = _swig_property(_swiggimp.aiVertexWeight_mVertexId_get, _swiggimp.aiVertexWeight_mVertexId_set)
    __swig_setmethods__["mWeight"] = _swiggimp.aiVertexWeight_mWeight_set
    __swig_getmethods__["mWeight"] = _swiggimp.aiVertexWeight_mWeight_get
    if _newclass:mWeight = _swig_property(_swiggimp.aiVertexWeight_mWeight_get, _swiggimp.aiVertexWeight_mWeight_set)
    def __init__(self, *args): 
        this = _swiggimp.new_aiVertexWeight(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_aiVertexWeight
    __del__ = lambda self : None;
aiVertexWeight_swigregister = _swiggimp.aiVertexWeight_swigregister
aiVertexWeight_swigregister(aiVertexWeight)

class aiBone(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiBone, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiBone, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mName"] = _swiggimp.aiBone_mName_set
    __swig_getmethods__["mName"] = _swiggimp.aiBone_mName_get
    if _newclass:mName = _swig_property(_swiggimp.aiBone_mName_get, _swiggimp.aiBone_mName_set)
    __swig_setmethods__["mNumWeights"] = _swiggimp.aiBone_mNumWeights_set
    __swig_getmethods__["mNumWeights"] = _swiggimp.aiBone_mNumWeights_get
    if _newclass:mNumWeights = _swig_property(_swiggimp.aiBone_mNumWeights_get, _swiggimp.aiBone_mNumWeights_set)
    __swig_setmethods__["mWeights"] = _swiggimp.aiBone_mWeights_set
    __swig_getmethods__["mWeights"] = _swiggimp.aiBone_mWeights_get
    if _newclass:mWeights = _swig_property(_swiggimp.aiBone_mWeights_get, _swiggimp.aiBone_mWeights_set)
    __swig_setmethods__["mOffsetMatrix"] = _swiggimp.aiBone_mOffsetMatrix_set
    __swig_getmethods__["mOffsetMatrix"] = _swiggimp.aiBone_mOffsetMatrix_get
    if _newclass:mOffsetMatrix = _swig_property(_swiggimp.aiBone_mOffsetMatrix_get, _swiggimp.aiBone_mOffsetMatrix_set)
    def __init__(self, *args): 
        this = _swiggimp.new_aiBone(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_aiBone
    __del__ = lambda self : None;
aiBone_swigregister = _swiggimp.aiBone_swigregister
aiBone_swigregister(aiBone)

aiPrimitiveType_POINT = _swiggimp.aiPrimitiveType_POINT
aiPrimitiveType_LINE = _swiggimp.aiPrimitiveType_LINE
aiPrimitiveType_TRIANGLE = _swiggimp.aiPrimitiveType_TRIANGLE
aiPrimitiveType_POLYGON = _swiggimp.aiPrimitiveType_POLYGON
class aiAnimMesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiAnimMesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiAnimMesh, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mVertices"] = _swiggimp.aiAnimMesh_mVertices_set
    __swig_getmethods__["mVertices"] = _swiggimp.aiAnimMesh_mVertices_get
    if _newclass:mVertices = _swig_property(_swiggimp.aiAnimMesh_mVertices_get, _swiggimp.aiAnimMesh_mVertices_set)
    __swig_setmethods__["mNormals"] = _swiggimp.aiAnimMesh_mNormals_set
    __swig_getmethods__["mNormals"] = _swiggimp.aiAnimMesh_mNormals_get
    if _newclass:mNormals = _swig_property(_swiggimp.aiAnimMesh_mNormals_get, _swiggimp.aiAnimMesh_mNormals_set)
    __swig_setmethods__["mTangents"] = _swiggimp.aiAnimMesh_mTangents_set
    __swig_getmethods__["mTangents"] = _swiggimp.aiAnimMesh_mTangents_get
    if _newclass:mTangents = _swig_property(_swiggimp.aiAnimMesh_mTangents_get, _swiggimp.aiAnimMesh_mTangents_set)
    __swig_setmethods__["mBitangents"] = _swiggimp.aiAnimMesh_mBitangents_set
    __swig_getmethods__["mBitangents"] = _swiggimp.aiAnimMesh_mBitangents_get
    if _newclass:mBitangents = _swig_property(_swiggimp.aiAnimMesh_mBitangents_get, _swiggimp.aiAnimMesh_mBitangents_set)
    __swig_setmethods__["mColors"] = _swiggimp.aiAnimMesh_mColors_set
    __swig_getmethods__["mColors"] = _swiggimp.aiAnimMesh_mColors_get
    if _newclass:mColors = _swig_property(_swiggimp.aiAnimMesh_mColors_get, _swiggimp.aiAnimMesh_mColors_set)
    __swig_setmethods__["mTextureCoords"] = _swiggimp.aiAnimMesh_mTextureCoords_set
    __swig_getmethods__["mTextureCoords"] = _swiggimp.aiAnimMesh_mTextureCoords_get
    if _newclass:mTextureCoords = _swig_property(_swiggimp.aiAnimMesh_mTextureCoords_get, _swiggimp.aiAnimMesh_mTextureCoords_set)
    __swig_setmethods__["mNumVertices"] = _swiggimp.aiAnimMesh_mNumVertices_set
    __swig_getmethods__["mNumVertices"] = _swiggimp.aiAnimMesh_mNumVertices_get
    if _newclass:mNumVertices = _swig_property(_swiggimp.aiAnimMesh_mNumVertices_get, _swiggimp.aiAnimMesh_mNumVertices_set)
    def __init__(self): 
        this = _swiggimp.new_aiAnimMesh()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_aiAnimMesh
    __del__ = lambda self : None;
    def HasPositions(self): return _swiggimp.aiAnimMesh_HasPositions(self)
    def HasNormals(self): return _swiggimp.aiAnimMesh_HasNormals(self)
    def HasTangentsAndBitangents(self): return _swiggimp.aiAnimMesh_HasTangentsAndBitangents(self)
    def HasVertexColors(self, *args): return _swiggimp.aiAnimMesh_HasVertexColors(self, *args)
    def HasTextureCoords(self, *args): return _swiggimp.aiAnimMesh_HasTextureCoords(self, *args)
aiAnimMesh_swigregister = _swiggimp.aiAnimMesh_swigregister
aiAnimMesh_swigregister(aiAnimMesh)

class aiMesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, aiMesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, aiMesh, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mPrimitiveTypes"] = _swiggimp.aiMesh_mPrimitiveTypes_set
    __swig_getmethods__["mPrimitiveTypes"] = _swiggimp.aiMesh_mPrimitiveTypes_get
    if _newclass:mPrimitiveTypes = _swig_property(_swiggimp.aiMesh_mPrimitiveTypes_get, _swiggimp.aiMesh_mPrimitiveTypes_set)
    __swig_setmethods__["mNumVertices"] = _swiggimp.aiMesh_mNumVertices_set
    __swig_getmethods__["mNumVertices"] = _swiggimp.aiMesh_mNumVertices_get
    if _newclass:mNumVertices = _swig_property(_swiggimp.aiMesh_mNumVertices_get, _swiggimp.aiMesh_mNumVertices_set)
    __swig_setmethods__["mNumFaces"] = _swiggimp.aiMesh_mNumFaces_set
    __swig_getmethods__["mNumFaces"] = _swiggimp.aiMesh_mNumFaces_get
    if _newclass:mNumFaces = _swig_property(_swiggimp.aiMesh_mNumFaces_get, _swiggimp.aiMesh_mNumFaces_set)
    __swig_setmethods__["mVertices"] = _swiggimp.aiMesh_mVertices_set
    __swig_getmethods__["mVertices"] = _swiggimp.aiMesh_mVertices_get
    if _newclass:mVertices = _swig_property(_swiggimp.aiMesh_mVertices_get, _swiggimp.aiMesh_mVertices_set)
    __swig_setmethods__["mNormals"] = _swiggimp.aiMesh_mNormals_set
    __swig_getmethods__["mNormals"] = _swiggimp.aiMesh_mNormals_get
    if _newclass:mNormals = _swig_property(_swiggimp.aiMesh_mNormals_get, _swiggimp.aiMesh_mNormals_set)
    __swig_setmethods__["mTangents"] = _swiggimp.aiMesh_mTangents_set
    __swig_getmethods__["mTangents"] = _swiggimp.aiMesh_mTangents_get
    if _newclass:mTangents = _swig_property(_swiggimp.aiMesh_mTangents_get, _swiggimp.aiMesh_mTangents_set)
    __swig_setmethods__["mBitangents"] = _swiggimp.aiMesh_mBitangents_set
    __swig_getmethods__["mBitangents"] = _swiggimp.aiMesh_mBitangents_get
    if _newclass:mBitangents = _swig_property(_swiggimp.aiMesh_mBitangents_get, _swiggimp.aiMesh_mBitangents_set)
    __swig_setmethods__["mColors"] = _swiggimp.aiMesh_mColors_set
    __swig_getmethods__["mColors"] = _swiggimp.aiMesh_mColors_get
    if _newclass:mColors = _swig_property(_swiggimp.aiMesh_mColors_get, _swiggimp.aiMesh_mColors_set)
    __swig_setmethods__["mTextureCoords"] = _swiggimp.aiMesh_mTextureCoords_set
    __swig_getmethods__["mTextureCoords"] = _swiggimp.aiMesh_mTextureCoords_get
    if _newclass:mTextureCoords = _swig_property(_swiggimp.aiMesh_mTextureCoords_get, _swiggimp.aiMesh_mTextureCoords_set)
    __swig_setmethods__["mNumUVComponents"] = _swiggimp.aiMesh_mNumUVComponents_set
    __swig_getmethods__["mNumUVComponents"] = _swiggimp.aiMesh_mNumUVComponents_get
    if _newclass:mNumUVComponents = _swig_property(_swiggimp.aiMesh_mNumUVComponents_get, _swiggimp.aiMesh_mNumUVComponents_set)
    __swig_setmethods__["mFaces"] = _swiggimp.aiMesh_mFaces_set
    __swig_getmethods__["mFaces"] = _swiggimp.aiMesh_mFaces_get
    if _newclass:mFaces = _swig_property(_swiggimp.aiMesh_mFaces_get, _swiggimp.aiMesh_mFaces_set)
    __swig_setmethods__["mNumBones"] = _swiggimp.aiMesh_mNumBones_set
    __swig_getmethods__["mNumBones"] = _swiggimp.aiMesh_mNumBones_get
    if _newclass:mNumBones = _swig_property(_swiggimp.aiMesh_mNumBones_get, _swiggimp.aiMesh_mNumBones_set)
    __swig_setmethods__["mBones"] = _swiggimp.aiMesh_mBones_set
    __swig_getmethods__["mBones"] = _swiggimp.aiMesh_mBones_get
    if _newclass:mBones = _swig_property(_swiggimp.aiMesh_mBones_get, _swiggimp.aiMesh_mBones_set)
    __swig_setmethods__["mMaterialIndex"] = _swiggimp.aiMesh_mMaterialIndex_set
    __swig_getmethods__["mMaterialIndex"] = _swiggimp.aiMesh_mMaterialIndex_get
    if _newclass:mMaterialIndex = _swig_property(_swiggimp.aiMesh_mMaterialIndex_get, _swiggimp.aiMesh_mMaterialIndex_set)
    __swig_setmethods__["mName"] = _swiggimp.aiMesh_mName_set
    __swig_getmethods__["mName"] = _swiggimp.aiMesh_mName_get
    if _newclass:mName = _swig_property(_swiggimp.aiMesh_mName_get, _swiggimp.aiMesh_mName_set)
    __swig_setmethods__["mNumAnimMeshes"] = _swiggimp.aiMesh_mNumAnimMeshes_set
    __swig_getmethods__["mNumAnimMeshes"] = _swiggimp.aiMesh_mNumAnimMeshes_get
    if _newclass:mNumAnimMeshes = _swig_property(_swiggimp.aiMesh_mNumAnimMeshes_get, _swiggimp.aiMesh_mNumAnimMeshes_set)
    __swig_setmethods__["mAnimMeshes"] = _swiggimp.aiMesh_mAnimMeshes_set
    __swig_getmethods__["mAnimMeshes"] = _swiggimp.aiMesh_mAnimMeshes_get
    if _newclass:mAnimMeshes = _swig_property(_swiggimp.aiMesh_mAnimMeshes_get, _swiggimp.aiMesh_mAnimMeshes_set)
    def __init__(self): 
        this = _swiggimp.new_aiMesh()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_aiMesh
    __del__ = lambda self : None;
    def HasPositions(self): return _swiggimp.aiMesh_HasPositions(self)
    def HasFaces(self): return _swiggimp.aiMesh_HasFaces(self)
    def HasNormals(self): return _swiggimp.aiMesh_HasNormals(self)
    def HasTangentsAndBitangents(self): return _swiggimp.aiMesh_HasTangentsAndBitangents(self)
    def HasVertexColors(self, *args): return _swiggimp.aiMesh_HasVertexColors(self, *args)
    def HasTextureCoords(self, *args): return _swiggimp.aiMesh_HasTextureCoords(self, *args)
    def GetNumUVChannels(self): return _swiggimp.aiMesh_GetNumUVChannels(self)
    def GetNumColorChannels(self): return _swiggimp.aiMesh_GetNumColorChannels(self)
    def HasBones(self): return _swiggimp.aiMesh_HasBones(self)
    def vertexValues(self): return _swiggimp.aiMesh_vertexValues(self)
    __swig_getmethods__["valueAt"] = lambda x: _swiggimp.aiMesh_valueAt
    if _newclass:valueAt = staticmethod(_swiggimp.aiMesh_valueAt)
aiMesh_swigregister = _swiggimp.aiMesh_swigregister
aiMesh_swigregister(aiMesh)

def aiMesh_valueAt(*args):
  return _swiggimp.aiMesh_valueAt(*args)
aiMesh_valueAt = _swiggimp.aiMesh_valueAt

AI_PROPERTY_WAS_NOT_EXISTING = _swiggimp.AI_PROPERTY_WAS_NOT_EXISTING
class Importer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Importer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Importer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _swiggimp.new_Importer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _swiggimp.delete_Importer
    __del__ = lambda self : None;
    def RegisterLoader(self, *args): return _swiggimp.Importer_RegisterLoader(self, *args)
    def UnregisterLoader(self, *args): return _swiggimp.Importer_UnregisterLoader(self, *args)
    def RegisterPPStep(self, *args): return _swiggimp.Importer_RegisterPPStep(self, *args)
    def UnregisterPPStep(self, *args): return _swiggimp.Importer_UnregisterPPStep(self, *args)
    def SetPropertyInteger(self, *args): return _swiggimp.Importer_SetPropertyInteger(self, *args)
    def SetPropertyBool(self, *args): return _swiggimp.Importer_SetPropertyBool(self, *args)
    def SetPropertyFloat(self, *args): return _swiggimp.Importer_SetPropertyFloat(self, *args)
    def SetPropertyString(self, *args): return _swiggimp.Importer_SetPropertyString(self, *args)
    def SetPropertyMatrix(self, *args): return _swiggimp.Importer_SetPropertyMatrix(self, *args)
    def GetPropertyInteger(self, *args): return _swiggimp.Importer_GetPropertyInteger(self, *args)
    def GetPropertyBool(self, *args): return _swiggimp.Importer_GetPropertyBool(self, *args)
    def GetPropertyFloat(self, *args): return _swiggimp.Importer_GetPropertyFloat(self, *args)
    def GetPropertyString(self, *args): return _swiggimp.Importer_GetPropertyString(self, *args)
    def GetPropertyMatrix(self, *args): return _swiggimp.Importer_GetPropertyMatrix(self, *args)
    def SetIOHandler(self, *args): return _swiggimp.Importer_SetIOHandler(self, *args)
    def GetIOHandler(self): return _swiggimp.Importer_GetIOHandler(self)
    def IsDefaultIOHandler(self): return _swiggimp.Importer_IsDefaultIOHandler(self)
    def SetProgressHandler(self, *args): return _swiggimp.Importer_SetProgressHandler(self, *args)
    def GetProgressHandler(self): return _swiggimp.Importer_GetProgressHandler(self)
    def IsDefaultProgressHandler(self): return _swiggimp.Importer_IsDefaultProgressHandler(self)
    def ValidateFlags(self, *args): return _swiggimp.Importer_ValidateFlags(self, *args)
    def ReadFileFromMemory(self, *args): return _swiggimp.Importer_ReadFileFromMemory(self, *args)
    def ApplyPostProcessing(self, *args): return _swiggimp.Importer_ApplyPostProcessing(self, *args)
    def ReadFile(self, *args): return _swiggimp.Importer_ReadFile(self, *args)
    def FreeScene(self): return _swiggimp.Importer_FreeScene(self)
    def GetErrorString(self): return _swiggimp.Importer_GetErrorString(self)
    def GetScene(self): return _swiggimp.Importer_GetScene(self)
    def GetOrphanedScene(self): return _swiggimp.Importer_GetOrphanedScene(self)
    def IsExtensionSupported(self, *args): return _swiggimp.Importer_IsExtensionSupported(self, *args)
    def GetExtensionList(self, *args): return _swiggimp.Importer_GetExtensionList(self, *args)
    def GetImporterCount(self): return _swiggimp.Importer_GetImporterCount(self)
    def GetImporterInfo(self, *args): return _swiggimp.Importer_GetImporterInfo(self, *args)
    def GetImporter(self, *args): return _swiggimp.Importer_GetImporter(self, *args)
    def GetImporterIndex(self, *args): return _swiggimp.Importer_GetImporterIndex(self, *args)
    def GetMemoryRequirements(self, *args): return _swiggimp.Importer_GetMemoryRequirements(self, *args)
    def SetExtraVerbose(self, *args): return _swiggimp.Importer_SetExtraVerbose(self, *args)
    def Pimpl(self, *args): return _swiggimp.Importer_Pimpl(self, *args)
Importer_swigregister = _swiggimp.Importer_swigregister
Importer_swigregister(Importer)

aiProcess_CalcTangentSpace = _swiggimp.aiProcess_CalcTangentSpace
aiProcess_JoinIdenticalVertices = _swiggimp.aiProcess_JoinIdenticalVertices
aiProcess_MakeLeftHanded = _swiggimp.aiProcess_MakeLeftHanded
aiProcess_Triangulate = _swiggimp.aiProcess_Triangulate
aiProcess_RemoveComponent = _swiggimp.aiProcess_RemoveComponent
aiProcess_GenNormals = _swiggimp.aiProcess_GenNormals
aiProcess_GenSmoothNormals = _swiggimp.aiProcess_GenSmoothNormals
aiProcess_SplitLargeMeshes = _swiggimp.aiProcess_SplitLargeMeshes
aiProcess_PreTransformVertices = _swiggimp.aiProcess_PreTransformVertices
aiProcess_LimitBoneWeights = _swiggimp.aiProcess_LimitBoneWeights
aiProcess_ValidateDataStructure = _swiggimp.aiProcess_ValidateDataStructure
aiProcess_ImproveCacheLocality = _swiggimp.aiProcess_ImproveCacheLocality
aiProcess_RemoveRedundantMaterials = _swiggimp.aiProcess_RemoveRedundantMaterials
aiProcess_FixInfacingNormals = _swiggimp.aiProcess_FixInfacingNormals
aiProcess_SortByPType = _swiggimp.aiProcess_SortByPType
aiProcess_FindDegenerates = _swiggimp.aiProcess_FindDegenerates
aiProcess_FindInvalidData = _swiggimp.aiProcess_FindInvalidData
aiProcess_GenUVCoords = _swiggimp.aiProcess_GenUVCoords
aiProcess_TransformUVCoords = _swiggimp.aiProcess_TransformUVCoords
aiProcess_FindInstances = _swiggimp.aiProcess_FindInstances
aiProcess_OptimizeMeshes = _swiggimp.aiProcess_OptimizeMeshes
aiProcess_OptimizeGraph = _swiggimp.aiProcess_OptimizeGraph
aiProcess_FlipUVs = _swiggimp.aiProcess_FlipUVs
aiProcess_FlipWindingOrder = _swiggimp.aiProcess_FlipWindingOrder
aiProcess_SplitByBoneCount = _swiggimp.aiProcess_SplitByBoneCount
aiProcess_Debone = _swiggimp.aiProcess_Debone
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _swiggimp.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _swiggimp.SwigPyIterator_value(self)
    def incr(self, n=1): return _swiggimp.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _swiggimp.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _swiggimp.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _swiggimp.SwigPyIterator_equal(self, *args)
    def copy(self): return _swiggimp.SwigPyIterator_copy(self)
    def next(self): return _swiggimp.SwigPyIterator_next(self)
    def __next__(self): return _swiggimp.SwigPyIterator___next__(self)
    def previous(self): return _swiggimp.SwigPyIterator_previous(self)
    def advance(self, *args): return _swiggimp.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _swiggimp.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _swiggimp.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _swiggimp.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _swiggimp.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _swiggimp.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _swiggimp.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _swiggimp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _swiggimp.FloatVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _swiggimp.FloatVector___nonzero__(self)
    def __bool__(self): return _swiggimp.FloatVector___bool__(self)
    def __len__(self): return _swiggimp.FloatVector___len__(self)
    def pop(self): return _swiggimp.FloatVector_pop(self)
    def __getslice__(self, *args): return _swiggimp.FloatVector___getslice__(self, *args)
    def __setslice__(self, *args): return _swiggimp.FloatVector___setslice__(self, *args)
    def __delslice__(self, *args): return _swiggimp.FloatVector___delslice__(self, *args)
    def __delitem__(self, *args): return _swiggimp.FloatVector___delitem__(self, *args)
    def __getitem__(self, *args): return _swiggimp.FloatVector___getitem__(self, *args)
    def __setitem__(self, *args): return _swiggimp.FloatVector___setitem__(self, *args)
    def append(self, *args): return _swiggimp.FloatVector_append(self, *args)
    def empty(self): return _swiggimp.FloatVector_empty(self)
    def size(self): return _swiggimp.FloatVector_size(self)
    def clear(self): return _swiggimp.FloatVector_clear(self)
    def swap(self, *args): return _swiggimp.FloatVector_swap(self, *args)
    def get_allocator(self): return _swiggimp.FloatVector_get_allocator(self)
    def begin(self): return _swiggimp.FloatVector_begin(self)
    def end(self): return _swiggimp.FloatVector_end(self)
    def rbegin(self): return _swiggimp.FloatVector_rbegin(self)
    def rend(self): return _swiggimp.FloatVector_rend(self)
    def pop_back(self): return _swiggimp.FloatVector_pop_back(self)
    def erase(self, *args): return _swiggimp.FloatVector_erase(self, *args)
    def __init__(self, *args): 
        this = _swiggimp.new_FloatVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _swiggimp.FloatVector_push_back(self, *args)
    def front(self): return _swiggimp.FloatVector_front(self)
    def back(self): return _swiggimp.FloatVector_back(self)
    def assign(self, *args): return _swiggimp.FloatVector_assign(self, *args)
    def resize(self, *args): return _swiggimp.FloatVector_resize(self, *args)
    def insert(self, *args): return _swiggimp.FloatVector_insert(self, *args)
    def reserve(self, *args): return _swiggimp.FloatVector_reserve(self, *args)
    def capacity(self): return _swiggimp.FloatVector_capacity(self)
    __swig_destroy__ = _swiggimp.delete_FloatVector
    __del__ = lambda self : None;
FloatVector_swigregister = _swiggimp.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

# This file is compatible with both classic and new-style classes.

