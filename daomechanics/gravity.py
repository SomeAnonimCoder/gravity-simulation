import numpy as np

"""
https://beltoforion.de/article.php?a=barnes-hut-galaxy-simulator
The Barnes-Hut algorithm
"""
"""
 
Function MainApp::CalcForce
  for all particles
    force = RootNode.CalculateForceFromTree(particle)
  end for
end 

Function force = TreeNode::CalculateForce(targetParticle)
  force = 0

  if number of particle equals 1
    force = Gravitational force between targetParticle and particle
  else
    r = distance from nodes center of mass to targetParticle
    d = height of the node
    if (d/r < θ)
      force = Gravitational force between targetParticle and node 
    else
      for all child nodes n
        force += n.CalculateForce(particle)
      end for
    end if
  end
end
"""


class Body:
    def __init__(self, mass, x0, y0, v0_1, v0_2):
        self.mass = mass
        self.x1 = x0
        self.x2 = y0
        self.v1 = v0_1
        self.v2 = v0_2
        self.x_args = [x0]
        self.y_args = [y0]
        self.v1_args = [v0_1]
        self.v2_args = [v0_2]

    def get_mass(self):
        return self.mass

    def set_coord(self, x, y):
        self.x1 = x
        self.x2 = y
        self.x_args.append(x)
        self.y_args.append(y)

    def set_velocity(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.v1_args.append(v1)
        self.v2_args.append(v2)

    def get_init_cordinates(self):
        return np.array([self.x0_1, self.x0_2])

    def get_init_velocity(self):
        return np.array([self.v0_1, self.v0_2])

    def get_x_args(self):
        return self.x_args

    def set_y_args(self):
        return self.y_args

    def __str__(self):
        return  "[" +str( self.x1) + "," + str(self.x2) + "]" + "- mass : " + str(self.mass)


class NodeBody:
    def __init__(self, body, range=[4, 4]):
        self.body = body
        """
         Quadrants
        |11|12' 
        |21|22|
        _
        """
        self.root = None
        self.Q_11 = None  # Quadrant 11
        self.Q_12 = None  # Quadrant 12
        self.Q_21 = None  # Quadrant 21
        self.Q_22 = None  # Quadrant 22

    def __add__(self, node, body):
        if body.x1 <= node.body.x1 and body.x2 >= node.body.x2:
            if node.Q_11 is None:
                node.Q_11 = NodeBody(body)
                return
            self.__add__(node.Q_11, body)
        elif body.x1 >= node.body.x1 and body.x2 >= node.body.x2:
            if node.Q_12 is None:
                node.Q_12 = NodeBody(body)
                return
            self.__add__(node.Q_12, body)
        elif body.x1 <= node.body.x1 and body.x2 <= node.body.x2:
            if node.Q_21 is None:
                node.Q_21 = NodeBody(body)
                return
            self.__add__(node.Q_11, body)
        elif body.x1 >= node.body.x1 and body.x2 <= node.body.x2:
            if node.Q_22 is None:
                node.Q_22 = NodeBody(body)
                return
            self.__add__(node.Q_11, body)

    def compute_center_of_mass(self):
        """
         this will comute center mmass for each node
        :return:
        """
        pass

    def iterate(self):
        if self.Q_11 is not None:
            self.Q_11.iterate()
        print(self.body.__str__())
        self.execute(None)

        if self.Q_21 is not None:
            self.Q_21.iterate()

        if self.Q_12 is not None:
            self.Q_12.iterate()
        if self.Q_22 is not None:
            self.Q_22.iterate()


class TreeBody:
    def __init__(self):
        self.root = None;

    def add_element(self, body):
        if self.root is None:
            self.root = NodeBody(body)

        else:
            self.root.__add__(self.root, body)

    def print(self):
        self.root.iterate()



    def compute_center_mass_node(self,node):
        """

        :param node: nodeBody
        :return: center of mass as sum of all bodyes with root given node
        """
        pass

    def compare(self,distance,node):
        """

        comparing W/R
        where W - width of the region of node
        R distance between body and node
        :param distance:
        :param node:
        :return:
        """
        pass

    def calculate_velocity(self,node):
        pass




class Ground:
    def __init__(self):
        self.bodies = []
        self.tree = TreeBody()

    def add_body(self, body):
        self.bodies.append(body)
        self.tree.add_element(body)
    def print(self):
        self.tree.print()


"""
Force Calculation 
d - Size of box
r - Partical distance for nodes center of mass

k = d/r

If θ lies below a certain threshold the force 
can be approximated by inserting the quadrant nodes 
mass and its center of mass in the law of gravity. 
The child nodes don't have to be summed up separately.
 A reasonable relation is k < 1. If θ
  is larger than the threshold the quadrants effect can't be 
  approximated and all of its child nodes have to be tested again. The iteration stops only after all nodes have been tested. 
  The worst case scenario is having to test all nodes without finding any node that meets the MAC. In such a case the result 
  is similar to summing up all mutual particle forces (θ=0). 
  The iteration depth can be finetuned by adjusting θ. Animation 1 illustrates 
the influence of θ on the number of force computations

k = d/r

"""

###https://www.maths.tcd.ie/~btyrrel/nbody.pdf
### http://algorithm-interest-group.me/assets/slides/barnes_hut.pdf
### https://www.cs.vu.nl/ibis/papers/nijhuis_barnes_2004.pdf
##http://www.cs.hut.fi/~ctl/NBody.pdf
def center_mas():
    pass


g = Ground()
g.add_body(Body(32,0,0,1,1))
g.add_body(Body(32,1,1,1,1))
g.add_body(Body(32,2,3,1,1))
g.add_body(Body(32,-1,1,1,1))
g.print()