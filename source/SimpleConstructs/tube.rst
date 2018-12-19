
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)

.. index:: Tube

Tube
----

Now test function to make a tube generated along the z-axis
   
.. testcode::

   def tube(r, w, h, a ):
      ''' 
      Generate a (partial) tube with
      r  outside radius
      w  wall thickness
      h  length (height)
      a  angle of sweep (360 is full circle)
      e.g.
      b = tube(6, 2, 10, 90)
      ''' 
      b = Part.makeCylinder(r, h, Vector(0,0,0), Vector(0,0,1), a)
      b = b.cut(Part.makeCylinder(r-w, h, Vector(0,0,0), Vector(0,0,1), a))
      
      return(b)
  
Outside 6,  wall 2, length 10, angle of sweep  360 (round tube)
   
.. testcode::

   tb = tube( 6, 2, 10, 360)
   tb2 = tb.copy()
   tb2.rotate(O, Z, 30)
   testEqual(tb,  tb2)   # symmetric normal to z-axis
   tb2.rotate(O, X, 30)
   testNotEqual(tb,  tb2)  # not symmetric normal to x-axis
   
TEST generate a tube by revolving a rectangle (vs cutting two cylindars above)
   # edge1 = Part.makeLine((0,0,0), (10,0,0))
   
.. testcode::

   rect = Part.makePolygon([
        Vector(4,0,0), Vector(6,0,0),Vector(6,0,10),Vector(4,0,10), Vector(4,0,0)])
   
   tb3 = rect.revolve(O, Z, 360)
   # Part.show(tb3)
   testEqual(tb,  tb3)  

.. testcode::

   # outside 6,  wall 2, length 10, angle of sweep  90 (1/4 round)
   
   tb = tube( 6, 2, 10, 90)
   testEqual(tb,  tube(6, 2, 10, 90))
   testNotEqual(tb, tube(6, 2, 10, 80))

.. testcode::

   line = Part.LineSegment(O, Vector(10,0,0))
   edge = line.toShape() 
   
   if edge.Length != 10.0 : print('bad')
   
   if edge.CenterOfMass != Vector (5, 0, 0) : print('bad')
   
   
   edge1 = Part.makeLine((0,0,0), (10,0,0))
   edge2 = Part.makeLine((10,0,0), (10,10,0))
   wire1 = Part.Wire([edge1,edge2]) 
   edge3 = Part.makeLine((10,10,0), (0,10,0))
   edge4 = Part.makeLine((0,10,0), (0,0,0))
   wire2 = Part.Wire([edge3,edge4])
   wire3 = Part.Wire([wire1,wire2])
   wire3.Edges
   
   #Part.show(wire3) 

