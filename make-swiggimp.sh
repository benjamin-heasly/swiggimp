# http://www.swig.org/tutorial.html

# sudo apt-get install python-dev

# let swig generate code
swig -I/usr/local/include/assimp -python -c++ swiggimp.i

# compile the swig code
c++ -c -fPIC -I/usr/local/include/assimp -I/usr/include/python2.7/ swiggimp_wrap.cxx
c++ -shared swiggimp_wrap.o -o _swiggimp.so -L/usr/local/lib -lassimp

#python testImport.py

