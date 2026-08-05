class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty and sx != tx:
            if ty < tx:
                tx %= ty
            else:
                ty %= tx
        
        if sx == tx:
            return ty >= sy and (ty - sy) % sx == 0
        elif sy == ty:
            return tx >= sx and (tx - sx) % sy == 0
        
        return False