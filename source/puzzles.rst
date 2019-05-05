1/How does Part.Circle(o, z, 10) different from Part.makeCircle(10) 


2/
( following s.revolve help )

Why does this work

e = Part.Ellipse()
s = e.toShape()
r = s.revolve(o, y, 360) # this has artifacts because of doubling
Part.show(r)

and this

r = s.revolve(o, y, 180) # this still has artifacts because of no vertex
Part.show(r)

But not this

c10 = Part.Circle(o, z, 10) 
s10 = c10.toShape()
r = s10.revolve(o, y, 360)
Part.show(r)  # THERE SEEMS TO BE A BUG HERE

or this

r = s10.revolve(o, y, 180)
Part.show(r)  # THERE SEEMS TO BE A BUG HERE

3/
This is good but no idea what LastParameter/4 does to get half circle

s = c10.toShape(c10.LastParameter/4, 3*c10.LastParameter/4)
r = s.revolve(o, y, 360)
Part.show(r)

