""" Master Match Data """

__all__ = ["MasterMatch"]

from pandas import IntervalIndex, Interval
import math


###############################################################################
# Master List of Match Params
###############################################################################
class MasterMatch:
    def __init__(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        oflow = 2.0
        
        # Name
        nameBreaks = [0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0] + [oflow]
        self._nameInterval = IntervalIndex.from_breaks(nameBreaks, closed='left')
        
        # Media
        mediaBreaks = [0.7, 0.75, 0.8, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0] + [oflow]
        self._mediaInterval = IntervalIndex.from_breaks(mediaBreaks, closed='left')

        # Score
        oflow = 99.0
        
        mediaScoreBreaks = [0.0, 1.0, 1.3, 1.58, 1.75, 2.05, 2.35, 2.85] + [oflow]
        self._mediaScoreInterval = IntervalIndex.from_breaks(mediaScoreBreaks, closed='left')

        # Media Score Ratio
        oflow = 2.0
        mediaMatchRatioBreaks = [0.0, 0.7, 0.9] + [oflow]
        self._mediaMatchRatioInterval = IntervalIndex.from_breaks(mediaMatchRatioBreaks, closed='left')
        
        # Numerical Scoring
        self._mediaBaseWeights = {Interval(0.7, 0.75, closed='left'): 10.0, Interval(0.75, 0.8, closed='left'): 8.0,
                                  Interval(0.8, 0.85, closed='left'): 6.0, Interval(0.85, 0.875, closed='left'): 5.0,
                                  Interval(0.875, 0.9, closed='left'): 4.0, Interval(0.9, 0.925, closed='left'): 3.0,
                                  Interval(0.925, 0.95, closed='left'): 2.7, Interval(0.95, 0.975, closed='left'): 2.4,
                                  Interval(0.975, 1.0, closed='left'): 2.2, Interval(1.0, 2.0, closed='left'): 2.0}

        self._mediaScaleWeights = {Interval(0.7, 0.75, closed='left'): 9.0, Interval(0.75, 0.8, closed='left'): 6.0,
                                   Interval(0.8, 0.85, closed='left'): 4.0, Interval(0.85, 0.875, closed='left'): 2.0,
                                   Interval(0.875, 0.9, closed='left'): 2.0, Interval(0.9, 0.925, closed='left'): 1.5,
                                   Interval(0.925, 0.95, closed='left'): 1.5, Interval(0.95, 0.975, closed='left'): 1.0,
                                   Interval(0.975, 1.0, closed='left'): 1.0, Interval(1.0, 2.0, closed='left'): 1.0}
        
        Nscale = len(self._mediaScaleWeights)
        Nbase = len(self._mediaBaseWeights)
        Nint = len(self._mediaInterval)
        assert Nscale == Nbase, f"Must have equal lengths [Scale={Nscale}] vs [Base={Nbase}] for media weights"
        assert Nint == Nbase, f"Must have equal lengths [Interval={Nint}] vs [Scale/Base={Nbase}]"
    
        self.scoreFunc = self.log1pN
        
        self._cutoff = {"Name": min(nameBreaks), "Media": min(mediaBreaks)}
        
        if verbose is True:
            print("MasterMatch()")
            print("{0: <18}{1}".format("  ==> Cutoff:", self.cutoff))
            print("{0: <18}{1}".format("  ==> Name:", self.nameInterval))
            print("{0: <18}{1}".format("  ==> Media", self.mediaInterval))
            print("{0: <18}{1}".format("  ==> Media Score", self.mediaScoreInterval))
            print("{0: <18}{1}".format("  ==> Media fMatch", self.mediaMatchRatioInterval))
            print("{0: <18}{1}".format("  ==> Score", self.scoreFunc.__name__))
          
    def log1pN(self, x: int, scale: float, base: float) -> 'float':
        assert isinstance(scale, (float, int)) and scale > 0, f"Invalid scale: {scale}"
        assert isinstance(base, (float, int)) and base > 1, f"Invalid base: {base}"
        if not isinstance(x, int):
            return 0.0
        xValue = 1 + (x / scale)
        retval = math.log(xValue, base)
        return retval
    
    @property
    def mediaScaleWeights(self):
        return self._mediaScaleWeights

    @property
    def mediaBaseWeights(self):
        return self._mediaBaseWeights

    @property
    def cutoff(self):
        return self._cutoff
    
    @property
    def nameInterval(self):
        return self._nameInterval
    
    @property
    def mediaInterval(self):
        return self._mediaInterval
    
    @property
    def mediaScoreInterval(self):
        return self._mediaScoreInterval
    
    @property
    def mediaMatchRatioInterval(self):
        return self._mediaMatchRatioInterval