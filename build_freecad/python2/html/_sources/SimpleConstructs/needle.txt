
.. index:: Needle

Needle
------

# main shaft

a = Part.makeCylinder(1.0, 55, Vector(0, 0, 0), Vector(1, 0, 0), 360)
a = a.fuse(Part.makeSphere(1.0))
# Part.show(a)

# bent end shaft and point

b = Part.makeCylinder(1.0, 5, Vector(0, 0, 0), Vector(0, 0, 1), 360)
b1  = Part.makeCone(1.0, 0.3, 4)
b1.translate(Vector(0, 0, 5))
b2 = Part.makeSphere(0.3)
b2.translate(Vector(0, 0, 5+4))
b = b.fuse([b1, b2])
b.rotate(Vector(0, 0, 0), Vector(0.5, 1, 0), 90)
b.translate(Vector(55, 0, 0))
# Part.show(b)

# fill between shafts

c = Part.makeSphere(1.0)
c.translate(Vector(55, 0, 0))
# Part.show(c)

a = a.fuse([b, c])

# Part.show(a)

# hole for thread

# center origin, X , Y radii, default orientation  normal to z-axis
e = Part.Ellipse(o, 5, 0.4).toShape() 
e.translate(Vector(6, 0, -1))
d = Part.Face(Part.Wire(e)).extrude(Vector(0, 0, 5))
#Part.show(d) 
 
h = a.cut(d)
#Part.show(h) 

#  smooth thread hole edges

# cannot get fillet to work with these edges
#edges = []
#for e in h.Edges :
#   if (len(e.Vertexes) is 1) and e.Vertexes[0].Point[2] in (1.0, -1.0) :
#       edges.append(e)
#
#h = h.makeFillet(0.3, edges) 

# so cut out another ellipse across the top of the hole
# This leaves somewhat sharp edges
#This works in Freecad, but printing is a real problem because of the long
# bridge, and the sides areery narrow. Might try with a smaller nozzle.
# However, even without it the edges are too small to print with 0.4mm nozzle,
# or I have to make other adjustments I have not yet figured out.

# e = Part.Ellipse(Vector(0, 0, 0), 6, 0.3).toShape() 
# e.rotate(o,  x,  90)  # ceter at origin, about x-axis
# e.translate(Vector(6, -2, -1))
# d = Part.Face(Part.Wire(e)).extrude(Vector(0, 5, 0))
# #Part.show(d) 
# h = h.cut(d)
# 
# d.translate(Vector(0, 0, 2))
# h = h.cut(d)

#Part.show(h) 

m = MeshPart.meshFromShape(Shape= h, 
       LinearDeflection=0.1, AngularDeflection=0.523599, Relative=False)

# why both of these ?
Mesh.export([m],  "needle.stl")
m.write(Filename ="needle.stl")
