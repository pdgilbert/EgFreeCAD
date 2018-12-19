   
CLEAN UP BELOW

   wire3.Length
   > 40.0
   wire3.CenterOfMass
   > Vector (5, 5, 0)
   wire3.isClosed()
   > True
   wire2.isClosed()
   > False 
   
   face = Part.Face(wire3)
   face.Area
   > 99.999999999999972
   face.CenterOfMass
   > Vector (5, 5, 0)
   face.Length
   > 40.0
   face.isValid()
   > True
   sface = Part.Face(wire2)
   face.isValid()
   > False 
   
   
   arc = Part.Arc(Vector(0,0,0),Vector(0,5,0),Vector(5,5,0))
   arc
   > <Arc object>
   arc_edge = arc.toShape() 
   
   from math import pi
   circle = Part.Circle(Vector(0,0,0),Vector(0,0,1),10)
   arc = Part.Arc(c,0,pi) 
   
   lshape_wire = Part.makePolygon([Vector(0,5,0),Vector(0,0,0),Vector(5,0,0)]) 
   
   def makeBCurveEdge(Points):
      geomCurve = Part.BezierCurve()
      geomCurve.setPoles(Points)
      edge = Part.Edge(geomCurve)
      return(edge) 
   
   plane = Part.makePlane(2,2)
   plane
   ><Face object at 028AF990>
   plane = Part.makePlane(2,2, Vector(3,0,0), Vector(0,1,0))
   plane.BoundBox
   > BoundBox (3, 0, 0, 5, 0, 2) 
   
   
   
   # Generic transformations with matrixes
   
   myMat = Base.Matrix()
   myMat.move(Vector(2,0,0))
   myMat.rotateZ(math.pi/2)
   
   myMat.move(2,0,0)
   myMat.move(Vector(2,0,0))
   
   myShape.trasformShape(myMat)
   
   myShape.transformGeometry(myMat)
   
   myMat = Base.Matrix()
   myMat.scale(2,1,1)
   myShape=myShape.transformGeometry(myMat)
   
   cylinder = Part.makeCylinder(3,10,Vector(0,0,0),Vector(1,0,0))
   sphere = Part.makeSphere(5,Vector(5,0,0))
   diff = cylinder.cut(sphere)
   
   cylinder1 = Part.makeCylinder(3,10,Vector(0,0,0),Vector(1,0,0))
   cylinder2 = Part.makeCylinder(3,10,Vector(5,0,-5),Vector(0,0,1))
   common = cylinder1.common(cylinder2)
   
   cylinder1 = Part.makeCylinder(3,10,Vector(0,0,0),Vector(1,0,0))
   cylinder2 = Part.makeCylinder(3,10,Vector(5,0,-5),Vector(0,0,1))
   fuse = cylinder1.fuse(cylinder2)
   
   
   
   cylinder1 = Part.makeCylinder(3,10,Vector(0,0,0),Vector(1,0,0))
   cylinder2 = Part.makeCylinder(3,10,Vector(5,0,-5),Vector(0,0,1))
   section = cylinder1.section(cylinder2)
   section.Wires
   > []
   section.Edges
   > [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
    <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
    <Edge object at 0D8F4BB0>]
    
   circle = Part.makeCircle(10)
   tube = circle.extrude(Vector(0,0,2))
   
   wire = Part.Wire(circle)
   disc = Part.Face(wire)
   cylinder = disc.extrude(Vector(0,0,2))
   
   b = Part.makeBox(100,100,100)
   b.Wires
   w = b.Wires[0]
   w
   w.Wires
   w.Vertexes
   Part.show(w)
   w.Edges
   e = w.Edges[0]
   e.Vertexes
   v = e.Vertexes[0]
   v.Point
   
   box = Part.makeBox(100,100,100)
   anEdge = box.Edges[0]
   print anEdge.Length
   
   anEdge.tangentAt(0.0)      # tangent direction at the beginning
   anEdge.valueAt(0.0)        # Point at the beginning
   anEdge.valueAt(100.0)      # Point at the end of the edge
   anEdge.derivative1At(50.0) # first derivative of the curve in the middle
   anEdge.derivative2At(50.0) # second derivative of the curve in the middle
   anEdge.derivative3At(50.0) # third derivative of the curve in the middle
   anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
   anEdge.curvatureAt(50.0)   # the curvature
   anEdge.normalAt(50)        # normal vector at that position (if defined)
   
   Part.show(Part.makeBox(100,100,100))
   Gui.SendMsgToActiveView("ViewFit")
   
   for o in Gui.Selection.getSelectionEx():
                       print o.ObjectName
                       for s in o.SubElementNames:
                                           print "name: ",s
                       for s in o.SubObjects:
                                           print "object: ",s
   
   length = 0.0
   for o in Gui.Selection.getSelectionEx():
                       for s in o.SubObjects:
                                           length += s.Length
   print "Length of the selected edges:" ,length                               
   
   
   #Complete example: The OCC bottle
   
   import Part
   import MakeBottle
   bottle = MakeBottle.makeBottle()
   Part.show(bottle)
   
   bottle2 = bottle.copy
   bottle2.rotate(O, Z, 90)
   
   import Part, FreeCAD, math
   from FreeCAD import Base
   
   def makeBottle(myWidth=50.0, myHeight=70.0, myThickness=30.0):
      aPnt1=Vector(-myWidth/2.,0,0)
      aPnt2=Vector(-myWidth/2.,-myThickness/4.,0)
      aPnt3=Vector(0,-myThickness/2.,0)
      aPnt4=Vector(myWidth/2.,-myThickness/4.,0)
      aPnt5=Vector(myWidth/2.,0,0)
      
      aArcOfCircle = Part.Arc(aPnt2,aPnt3,aPnt4)
      aSegment1=Part.LineSegment(aPnt1,aPnt2)
      aSegment2=Part.LineSegment(aPnt4,aPnt5)
      aEdge1=aSegment1.toShape()
      aEdge2=aArcOfCircle.toShape()
      aEdge3=aSegment2.toShape()
      aWire=Part.Wire([aEdge1,aEdge2,aEdge3])
      
      aTrsf=Base.Matrix()
      aTrsf.rotateZ(math.pi) # rotate around the z-axis
      
      aMirroredWire=aWire.transformGeometry(aTrsf)
      myWireProfile=Part.Wire([aWire,aMirroredWire])
      myFaceProfile=Part.Face(myWireProfile)
      aPrismVec=Vector(0,0,myHeight)
      myBody=myFaceProfile.extrude(aPrismVec)
      myBody=myBody.makeFillet(myThickness/12.0,myBody.Edges)
      neckLocation=Vector(0,0,myHeight)
      neckNormal=Vector(0,0,1)
      myNeckRadius = myThickness / 4.
      myNeckHeight = myHeight / 10
      myNeck = Part.makeCylinder(myNeckRadius,myNeckHeight,neckLocation,neckNormal)                    
      myBody = myBody.fuse(myNeck)
      
      faceToRemove = 0
      zMax = -1.0
      
      for xp in myBody.Faces:
          try:
              surf = xp.Surface
              if type(surf) == Part.Plane:
                  z = surf.Position.z
                  if z > zMax:
                      zMax = z
                      faceToRemove = xp
          except:
              continue
      
      myBody = myBody.makeFillet(myThickness/12.0,myBody.Edges)
      
      return myBody
   
   el = makeBottle()
   Part.show(el)
   
   ### Box pierced
   
   import Draft, Part, FreeCAD, math, PartGui, FreeCADGui, PyQt4
   from math import sqrt, pi, sin, cos, asin
   from FreeCAD import Base
   
   size = 10
   poly = Part.makePolygon( [ (0,0,0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])
   
   face1 = Part.Face(poly)
   face2 = Part.Face(poly)
   face3 = Part.Face(poly)
   face4 = Part.Face(poly)
   face5 = Part.Face(poly)
   face6 = Part.Face(poly)
        
   myMat = FreeCAD.Matrix()
   myMat.rotateZ(math.pi/2)
   face2.transformShape(myMat)
   face2.translate(FreeCAD.Vector(size, 0, 0))
   
   myMat.rotateZ(math.pi/2)
   face3.transformShape(myMat)
   face3.translate(FreeCAD.Vector(size, size, 0))
   
   myMat.rotateZ(math.pi/2)
   face4.transformShape(myMat)
   face4.translate(FreeCAD.Vector(0, size, 0))
   
   myMat = FreeCAD.Matrix()
   myMat.rotateX(-math.pi/2)
   face5.transformShape(myMat)
   
   face6.transformShape(myMat)               
   face6.translate(FreeCAD.Vector(0,0,size))
   
   myShell = Part.makeShell([face1,face2,face3,face4,face5,face6])   
   
   mySolid = Part.makeSolid(myShell)
   mySolidRev = mySolid.copy()
   mySolidRev.reverse()
   
   myCyl = Part.makeCylinder(2,20)
   myCyl.translate(FreeCAD.Vector(size/2, size/2, 0))
   
   cut_part = mySolidRev.cut(myCyl)
   
   Part.show(cut_part)
   ##############################
