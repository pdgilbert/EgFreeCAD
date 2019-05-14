import Part, Mesh, MeshPart
#import math
from FreeCAD import Base, Vector

def isEmptyShape(a, debug = False):
   ''' 
   Test if shape a is empty. Return True if shape is empty, False otherwise.
   True is returned if a is None (not a shape) but False for other non-shapes.
   '''
   
   if a is None: 
      if debug : print("isEmptyShape returning True, object is None.")
      return(True)
   if not isinstance(a, Part.Shape): 
      if debug : print("isEmptyShape returning False, object is not a Shape.")
      return(False)
   
   if (0 != len(a.Vertexes)):
      if debug : print("isEmptyShape returning False, object has Vertexes.")
      return(False)

   # above is probably enough but ...
   if (0 != len(a.Edges)):
      if debug : print("isEmptyShape returning False, object has Edges.")
      return(False)
   if (0 != len(a.Faces)):
      if debug : print("isEmptyShape returning False, object has Faces.")
      return(False)
   if (0 != len(a.Shells)):
      if debug : print("isEmptyShape returning False, object has Shells.")
      return(False)
   if (0 != len(a.Wires)):
      if debug : print("isEmptyShape returning False, object has Wires.")
      return(False)

   if debug : print("isEmptyShape returning True, object is empty.")
   return(True)

def areEqual(a, b, debug = False):
   ''' 
   Test if shapes a and b are equal. Return True or False.
   Equal is in the sense of defining the same object in space,
   not in the sense of being similar python objects.
   The main part of this test is based on the observation that
   a.cut(b) and b.cut(a) should both be empty if the objects are equal.
   Empty means no Vertexes, Edges, Faces, ... .
   The first check is just for the case where a or b is empty, so cut will fail.
   The second check is for the case where a and b do not have the same ShapeType.
   This situation can reult in an empty object even though it should not.
   For example, cutting the face of a sphere from a solid sphere results in an
   empty object even though the first is hollow and the second is not. 
   '''
   
   if isEmptyShape(a, debug = debug):
      if isEmptyShape(b, debug = debug): return(True)
      else:          return(False)
   
   # punt if one is compound, but really should check if sub objects are same
   if a.ShapeType !=  'Compound' and b.ShapeType != 'Compound' : 
      if a.ShapeType != b.ShapeType :
         if debug : print("areEqual returning False, not the same ShapeType.")
         return(False)
   if not isEmptyShape(a.cut(b), debug = debug):    return(False)
   if not isEmptyShape(b.cut(a), debug = debug):    return(False)
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

def testEqual(a, b, debug = False):
   ''' 
   Use areEqual to check if shapes a and b are equal 
   and raise an exception if they are not.
   '''
   if not areEqual(a, b, debug = debug): raise Exception("Objects not equal")
   return(None)

def testNotEqual(a, b, debug = False):
   ''' 
   Use areEqual to check if shapes a and b are equal 
   and raise an exception if they are.
   '''
   if areEqual(a, b, debug = debug): raise Exception("Objects are equal")
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

