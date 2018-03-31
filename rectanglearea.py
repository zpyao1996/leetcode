class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1=(C-A)*(D-B)
        area2=(G-E)*(H-F)
        if C<E or B>H or G<A or F>D:
            area3=0
        else:
            [a,b]=[max(A,E),max(B,F)]
            [c,d]=[min(C,G),min(D,H)]
            area3=(c-a)*(d-b)
        return area1+area2-area3
