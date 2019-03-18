
.. index:: Foil

Foil
----

Project to extend a (hydro-) foil profile over a wing span outline.
   
.. testcode::
   
   #from __future__ import unicode_literals
   from FreeCAD import Base
   #import Draft, Part
   import Part, math
   
   class foil():
       
       class profile():
          def __init__(self, profileDAT, doc = None, source = None):
             self.profileDAT = profileDAT 
             self.doc        = doc
             self.source     = source
       
       class LeadTrail():
          def __init__(self, leadingEdge, trailingEdge, doc = None, source = None):
             self.leadingEdge  = leadingEdge
             self.trailingEdge = trailingEdge
             self.doc          = doc
             self.source       = source
       
       class construction():
          def __init__(self, profileList, rotation, leadingEdgeBspline, tailingEdgeBspline):
             self.profileList        = profileList
             self.rotation           = rotation
             self.leadingEdgeBspline = leadingEdgeBspline
             self.tailingEdgeBspline = tailingEdgeBspline
      
       def __init__(self, file_profile = None, file_LeadTrail = None,
                     profile = None, LeadTrail = None, foil = None, maxDegree=1):
           """
           Define a foil object with source file and construction information.
           The init method can specify source files file_profile, file_LeadTrail
           in which case they are loaded then constuction and foil are calculated.
           Otherwise ...
           """
           #   if not (-90 <= lat <= 90):
           #      raise ValueError("must have  -90 <=  latitude <= 90")
           
           if file_profile is not None:
               self.loadProfileDAT(file_profile)
           else:
               self.profile  =  profile #CLASS IS NOT EXTERNAL
               #self.profile(profileDAT, doc = profile_doc, source = file_profile)
           
           if file_LeadTrail is not None:
               self.loadLeadTrail(file_LeadTrail)
           else:
               self.profile  =  profile #CLASS IS NOT EXTERNAL
               #self.LeadTrail= self.LeadTrail(leadingEdge, trailingEdge,
               #                doc = LeadTrail_doc, source = file_LeadTrail)
           
           # Tried to use Part.BSplineCurve on the LeadingEdge and then makePipeShell
           #   self.foil = Part.Wire(
           #     self.construction.leadingEdgeBspline).makePipeShell(
           #       self.construction.profileList, True, False) #makeSolid, isFrenet)
           # but it gives twists and ripples in the trailing edge.
           # Just lofting the profiles seems to work better.
    
           #print("making traj wire.")
           #traj = Part.BSplineCurve()
           #traj.interpolate(self.LeadTrail.leadingEdge)       
           #leadingEdgeBspline = Part.Wire(traj.toShape())
           
           def scaledBspline(dat, sc):
              z = [FreeCAD.Vector(v[0]*sc, v[1]*sc, v[2]*sc) for v in dat]
              prof=Part.BSplineCurve()
              prof.interpolate(z)       
              prof=Part.Wire(prof.toShape())
              return prof
           
           print("calculating aprox. tangent (rotation) of the leading edge.")
           #angle adjustment Position is at leadingEndge rotate around cord.
           # The angle from X-Y plane determined by angle between tangent to 
           # leadingEdgeBspline and Z axis
           # this should really be the projection of the tangent onto the
           # plane defined by the cord being its normal. but for foils with the
           # cord aproximately in the direction of the X axis this will be aprox Dy/Dz.
           # Ends are one-sided tangent aprox, interior points use two adjacent
           Z = FreeCAD.Vector(0, 0, 1)
           e = self.LeadTrail.leadingEdge
           ln = len(e)
           rotation = [ Z.getAngle(e[1] - e[0])*180/math.pi ]
           for i  in range(ln - 2):
              rotation.append(Z.getAngle(e[i+2] - e[i])*180/math.pi)
           rotation.append(Z.getAngle(e[ln-1] - e[ln-2])*180/math.pi)
           
           print("building profileList.")
           profileList = []
           for ld, tr, r  in zip(self.LeadTrail.leadingEdge, 
                      self.LeadTrail.trailingEdge, rotation):
              #  zero case at tip cause scaling and rotation problems
              sc = ld.distanceToPoint(tr)
              if sc < 1e-2 :
                 sc =  1e-2
                 r  = 0.0
              p  = scaledBspline(self.profile.profileDAT, sc)
              print("scaled profile " + str(sc))
              p.translate(FreeCAD.Vector(ld))
              #angle adjustment
              # ld - tr or tr - ld reverse rotationBase.
              #FreeCADError: Unknown C++ exception
              print("ld, tr - ld, -r " + str(ld) + "," + str(tr - ld) + "," + str(-r))
              if (r != 0.0 ): p.rotate(ld, tr - ld, -r)
              profileList.append(p)
              print("rotated profile " + str(sc))
                   
           print("making EdgeBsplines.")
           tj = Part.BSplineCurve()
           tj.interpolate(self.LeadTrail.leadingEdge)       
           leadingEdgeBspline = Part.Wire(tj.toShape())
           
           tj = Part.BSplineCurve()
           tj.interpolate(self.LeadTrail.trailingEdge)       
           trailingEdgeBspline = Part.Wire(tj.toShape())
           
           self.construction = self.construction(profileList, rotation,
                                leadingEdgeBspline, trailingEdgeBspline)
           
           print("making foil.")
           #           Part.makeLoft(profileList, solid, ruled, closed, maxDegree)
           # The default maxDegree 5, and even 3, puts extra wabbles in straight edges,
           # unless there are many profiles. 1 seems enough for simple foil shapes.
           # It could be increased or made a parameter for more twisted shapes.
           
           self.foil = Part.makeLoft(profileList, True,  False, False, maxDegree) 
       
       def foil(self) :
          """Extract the foil FreeCAD object."""
          return(self.foil)
   
       def profileDAT(self) :
          """Extract profileDAT."""
          return(self.profile.profileDAT)
       
       def profileList(self) :
          """Extract profileList."""
          return(self.construction.profileList)
       
       def rotation(self) :
          """Extract rotation."""
          return(self.construction.rotation)
       
       def leadingEdgeBspline(self) :
          """Extract leadingEdgeBspline."""
          return(self.construction.leadingEdgeBspline)
       
       def trailingEdgeBspline(self) :
          """Extract trailingEdgeBspline."""
          return(self.construction.trailingEdgeBspline)
       
       def showProfiles(self) :
          """FreeCAD plot of profileList."""
          for p in self.construction.profileList: Part.show(p)
          return None
           
       def showfoil(self) :
          """FreeCAD plot of foil."""
          Part.show(self.foil)
          return None
       
       def showfoil2(self) :
          """FreeCAD plot of foil."""
          Part.show(self.foil2)
          return None
            
       def show(self) :
          """FreeCAD plot of foil, spline, and profiles."""
          self.showProfiles()
          self.showfoil()
          return None
           
       def loadProfileDAT(self, source):
           """read profile from a dat file and return it."""
           doc = []
           profileDAT =  []
           Z = 0.0
           print("loading profile.")
           with open(source) as f:  
              for i in f.readlines():
                 ln =  i.split()
                 ln = [b.strip()  for b in  ln]
                 #print(ln)
                 try : 
                    X = float(ln[0])
                    Y = float(ln[1])
                    #print(X, Y)
                    profileDAT.append(FreeCAD.Vector(X, Y, Z))
                 except :
                    doc.append(ln)
           
           self.profile = self.profile(profileDAT, doc=doc, source=source)
   
       def loadLeadTrail(self, source="/home/paul/CAD/foil/test.sweepPath"):
           """read Lead and Trailing edge data from file and return it."""
           doc =  []
           leadingEdge =  []
           trailingEdge = []
           print("loading leading and trailing edges.")
           with open(source) as f:  
              for i in f.readlines():
                 ln =  i.split()
                 ln = [b.strip()  for b in  ln]
                 #print(ln)
                 try : 
                    X = float(ln[0])
                    Y = float(ln[1])
                    Z = float(ln[2])
                    leadingEdge.append(FreeCAD.Vector(X, Y, Z))
                    X = float(ln[3])
                    Y = float(ln[4])
                    Z = float(ln[5])
                    trailingEdge.append(FreeCAD.Vector(X, Y, Z))
                 except :
                    doc.append(ln)
                
           self.LeadTrail = self.LeadTrail(leadingEdge,trailingEdge, doc=doc, source=source)
   
   
   z = foil(file_profile="/home/paul/CAD/foil/H105Coord.dat",
             file_LeadTrail="/home/paul/CAD/foil/test.sweepPath")
   z.show()
   
   #z.showfoil()  
   #z.showProfiles()
   #z.showBspline()
   
   z2 = foil(file_profile="/home/paul/CAD/foil/H105Coord.dat",
             file_LeadTrail="/home/paul/CAD/foil/test2.sweepPath")
   z2.show()
   
   z3 = foil(file_profile="/home/paul/CAD/foil/H105Coord.dat",
             file_LeadTrail="/home/paul/CAD/foil/test3.sweepPath",
             maxDegree=3)
   z3.show()
   
   
   # intersection of line and a plane
   
   Z  = FreeCAD.Vector( 0, 0, 1)
   
   p1 = FreeCAD.Vector( 100, 0, 1)
   p2 = FreeCAD.Vector(0, 100, 1)
   p3 = FreeCAD.Vector(-100, 0, 1)
   p4 = FreeCAD.Vector(0, -100, 1)
   
   # p is a surface (plane but bounded by points p*) because face=True
   p = Draft.makeWire([p1, p2, p3, p4], closed=True, face = True)
   zzz = Part.makeLine(FreeCAD.Vector(1,0, 0), FreeCAD.Vector(1,0, 10))
   dist,point,geom=zzz.distToShape(p.Shape)
   dist
   point
   geom
   
   # project vector onto spline 
   
   Z  = FreeCAD.Vector( 0, 0, 1)
   sp = z3.leadingEdgeBspline()
   
   zzz = Z.project(sp)
   zzzz = sp.project(Z)
   
   sp = z3.leadingEdgeBspline()
   zd = sp.discretize(20)
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
     
Put some text in here somewhere
