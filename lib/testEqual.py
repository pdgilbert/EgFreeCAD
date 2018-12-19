import Part, Mesh, MeshPart
#import math
from FreeCAD import Base, Vector

def isEmptyShape(a):
   ''' 
   Test if shape a is empty. Return True if shape is empty, False otherwise.
   True is returned if a is None (not a shape) but False for other non-shapes.
   '''
   
   if a is None: return(True)
   if not isinstance(a, Part.Shape): return(False)
   
   if (0 != len(a.Vertexes)): return(False)
   # above is probably enough but ...
   if (0 != len(a.Edges)):    return(False)
   if (0 != len(a.Faces)):   return(False)
   if (0 != len(a.Shells)):  return(False)
   if (0 != len(a.Wires)):   return(False)
   return(True)

def areEqual(a, b):
   ''' 
   Test if shapes a and b are equal. Return True or False.
   The main part of this test is based on the observation that
   a.cut(b) and b.cut(a) should both be empty if the objects are equal.
   The first checks are just for case where a or b is empty, so cut will fail.
   '''
   
   if isEmptyShape(a):
      if isEmptyShape(b): return(True)
      else:          return(False)
     
   if not isEmptyShape(a.cut(b)):    return(False)
   if not isEmptyShape(b.cut(a)):    return(False)
   return(True)

def isSubset(a, b):
   ''' 
   Test if shape a is a subset of b. Return True or False.
   Equality is considered to be a subset (True is returned).
   A strict subset is based on the observation that
   a.cut(b) is not empty but b.cut(a) is empty.
   The first checks are just for case where a or b is empty, so cut will fail.
   '''
   
   if isEmptyShape(a):  return(True)  #empty is always a subset
   
   if isEmptyShape(b):  return(False) #a and b empty would be True, but that is handled aboveempty is always a subset
   
   if areEqual(a,b):  return(True)
   
   # now for the case of strict subset   
   if     isEmptyShape(b.cut(a)) :  return(False)
   if not isEmptyShape(a.cut(b)) :  return(False)

   return(True)

def testEqual(a, b):
   ''' 
   Use areEqual to check if shapes a and b are equal 
   and raise an exception if they are not.
   '''
   if not areEqual(a, b): raise Exception("Objects not equal")
   return(None)

def testNotEqual(a, b):
   ''' 
   Use areEqual to check if shapes a and b are equal 
   and raise an exception if they are.
   '''
   if areEqual(a, b): raise Exception("Objects are equal")
   return(None)

def testSubset(a, b):
   ''' 
   Use isSubset to check if shape a is a (non-strict) subset of b 
   and raise an exception if it is not.
   '''
   if not isSubset(a, b): raise Exception("First object is not a subset of second.")
   return(None)

def testNotSubset(a, b):
   ''' 
   Use isSubset to check if shape a is not a (non-strict) subset of b 
   and raise an exception if it is.
   '''
   if isSubset(a, b): raise Exception("First object is a subset of second.")
   return(None)

def makeSTL(shp,  f) :
   ''' 
   THIS SHOULD BE areEqualMESH
   Generate an STL mesh file. shp is a shape object and 
   f is a string that will be appended with .stl for a file name.
   ''' 
   
   FreeCAD.Console.PrintMessage('generating stl file.\n')

   m = MeshPart.meshFromShape(Shape=shp, 
          LinearDeflection=0.1, AngularDeflection=0.523599, Relative=False)
   
   #mesh.ViewObject.CreaseAngle=25.0

   #Mesh.export([m], "./BT-" + f + ".stl")
   Mesh.export([m],  f + ".stl")
   m.write(Filename = f + ".stl")
   return None

