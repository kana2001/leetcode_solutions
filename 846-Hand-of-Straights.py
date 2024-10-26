class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False

        hand.sort()
        handFreq = {}
        for n in hand:
            handFreq[n] = handFreq.get(n, 0) + 1

        for n in hand:
            if (n - 1) not in handFreq and n in handFreq:
                currNum = n
                subsetLen = 1
                handFreq[n] -= 1
                if not handFreq[n]:
                    del handFreq[n]
                    
                while subsetLen < groupSize:
                    currNum += 1
                    if currNum not in handFreq:
                        return False
                    subsetLen += 1
                    handFreq[currNum] -= 1
                    if not handFreq[currNum]:
                        del handFreq[currNum]
        return True

        