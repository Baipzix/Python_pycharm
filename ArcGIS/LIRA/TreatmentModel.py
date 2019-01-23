import os
import pandas as pd
import numpy as np


# model for AVIE


def treat(reg, mr, sp, wet):
    tm = np.empty(reg.size, dtype=np.chararray)

    pine = np.logical_or(sp == 'Pine (Lodgepole/Jack)',
                         np.logical_or('Pine (Lodgepole/Jack) Mixedwood', 'Mixed Conifer (Pine - Lodgepole/Jack)'))
    whitespruce = np.logical_and(sp == 'White/Engelmann Spruce', sp == 'White/Engelmann Spruce')
    whitespruce_wl = np.logical_and(sp == 'White Spruce Wetland', sp == 'White Spruce Wetland')
    m_whitespruce = np.logical_or(sp == 'Mixed Conifer (White/Engelmann Spruce)',
                                  sp == 'White/Engelmann Spruce Mixedwood')
    m_blackspruce = np.logical_or(sp == 'Mixed Conifer (Black Spruce)', np.logical_or('True Fir', np.logical_or(
        'Black Spruce Mixedwood', 'True Fir Mixedwood')))
    blackspruce = np.logical_and(sp == 'Black Spruce', sp == 'Black Spruce')
    blackspruce_wl = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland', sp == 'Larch Tamarack Wetland')
    blackspruce_larch = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland',
                                      np.logical_or(sp == 'Larch Tamarack Wetland',
                                                    sp == 'Mixed Conifer (Larch Tamarack)'))
    industrial = np.logical_or(
        np.logical_or('Industrial Reclamation-Vegetated', 'Partial Cut/Regenerating Clearcut'),
        np.logical_or('Non-Veg ROWs', 'Herbaceous'))

    wetgraminiod = np.logical_or(np.logical_or('Bryophytic', 'Wet Graminoid'),
                                 np.logical_or('Grassland m', np.logical_or('Shrub Wetland', 'Grassland Mesic')))

    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), pine)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce_wl)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), industrial)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), pine)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce_wl)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), industrial)] = 'screef'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), pine)] = 'screef'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce_wl)] = 'screef'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_whitespruce)] = 'screef'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), industrial)] = 'screef'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), wetgraminiod)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), wetgraminiod)] = 'exclude'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'screef/mound'
    tm[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), wetgraminiod)] = 'exclude'

    reduce(tm)


def density1(reg, mr, sp, wet):
    dn1 = np.empty(reg.size, dtype=np.chararray)

    pine = np.logical_or(sp == 'Pine (Lodgepole/Jack)',
                         np.logical_or('Pine (Lodgepole/Jack) Mixedwood', 'Mixed Conifer (Pine - Lodgepole/Jack)'))
    whitespruce = np.logical_and(sp == 'White/Engelmann Spruce', sp == 'White/Engelmann Spruce')
    whitespruce_wl = np.logical_and(sp == 'White Spruce Wetland', sp == 'White Spruce Wetland')
    m_whitespruce = np.logical_or(sp == 'Mixed Conifer (White/Engelmann Spruce)',
                                  sp == 'White/Engelmann Spruce Mixedwood')
    m_blackspruce = np.logical_or(sp == 'Mixed Conifer (Black Spruce)', np.logical_or('True Fir', np.logical_or(
        'Black Spruce Mixedwood', 'True Fir Mixedwood')))
    blackspruce = np.logical_and(sp == 'Black Spruce', sp == 'Black Spruce')
    blackspruce_wl = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland', sp == 'Larch Tamarack Wetland')
    blackspruce_larch = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland',
                                      np.logical_or(sp == 'Larch Tamarack Wetland',
                                                    sp == 'Mixed Conifer (Larch Tamarack)'))
    industrial = np.logical_or(
        np.logical_or('Industrial Reclamation-Vegetated', 'Partial Cut/Regenerating Clearcut'),
        np.logical_or('Non-Veg ROWs', 'Herbaceous'))

    wetgraminiod = np.logical_or(np.logical_or('Bryophytic', 'Wet Graminoid'),
                                 np.logical_or('Grassland m', np.logical_or('Shrub Wetland', 'Grassland Mesic')))

    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce_wl)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_wl)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_larch)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), industrial)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), pine)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_larch)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), industrial)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce_wl)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_wl)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_larch)] = 'light Med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), industrial)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), pine)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_larch)] = 'medium small'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), industrial)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_larch)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), industrial)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce_wl)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_whitespruce)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce)] = 'light Med'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_wl)] = 'light Med'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_larch)] = 'light Med'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), industrial)] = 'light'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), pine)] = 'med'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_whitespruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_wl)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_larch)] = 'medium small'
    dn1[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), industrial)] = 'med'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'light'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'light large'
    dn1[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'med'

    reduce(dn1)


def planting(reg, mr, sp, wet):
    plt = np.empty(reg.size, dtype=np.chararray)

    pine = np.logical_or(sp == 'Pine (Lodgepole/Jack)',
                         np.logical_or('Pine (Lodgepole/Jack) Mixedwood', 'Mixed Conifer (Pine - Lodgepole/Jack)'))
    whitespruce = np.logical_and(sp == 'White/Engelmann Spruce', sp == 'White/Engelmann Spruce')
    whitespruce_wl = np.logical_and(sp == 'White Spruce Wetland', sp == 'White Spruce Wetland')
    m_whitespruce = np.logical_or(sp == 'Mixed Conifer (White/Engelmann Spruce)',
                                  sp == 'White/Engelmann Spruce Mixedwood')
    m_blackspruce = np.logical_or(sp == 'Mixed Conifer (Black Spruce)', np.logical_or('True Fir', np.logical_or(
        'Black Spruce Mixedwood', 'True Fir Mixedwood')))
    blackspruce = np.logical_and(sp == 'Black Spruce', sp == 'Black Spruce')
    blackspruce_wl = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland', sp == 'Larch Tamarack Wetland')
    blackspruce_larch = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland',
                                      np.logical_or(sp == 'Larch Tamarack Wetland',
                                                    sp == 'Mixed Conifer (Larch Tamarack)'))
    industrial = np.logical_or(
        np.logical_or('Industrial Reclamation-Vegetated', 'Partial Cut/Regenerating Clearcut'),
        np.logical_or('Non-Veg ROWs', 'Herbaceous'))

    wetgraminiod = np.logical_or(np.logical_or('Bryophytic', 'Wet Graminoid'),
                                 np.logical_or('Grassland m', np.logical_or('Shrub Wetland', 'Grassland Mesic')))

    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), pine)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), pine)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), pine)] = 'Pl'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), industrial)] = 'Pl'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'Pl Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'Sw'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'Sw Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'Sb Sw (Lt)'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'Sb'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'Sb Lt'
    plt[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'Pl'

    reduce(plt)


def density2(reg, mr, sp, wet):
    dn2 = np.empty(reg.size, dtype=np.chararray)

    pine = np.logical_or(sp == 'Pine (Lodgepole/Jack)',
                         np.logical_or('Pine (Lodgepole/Jack) Mixedwood', 'Mixed Conifer (Pine - Lodgepole/Jack)'))
    whitespruce = np.logical_and(sp == 'White/Engelmann Spruce', sp == 'White/Engelmann Spruce')
    whitespruce_wl = np.logical_and(sp == 'White Spruce Wetland', sp == 'White Spruce Wetland')
    m_whitespruce = np.logical_or(sp == 'Mixed Conifer (White/Engelmann Spruce)',
                                  sp == 'White/Engelmann Spruce Mixedwood')
    m_blackspruce = np.logical_or(sp == 'Mixed Conifer (Black Spruce)', np.logical_or('True Fir', np.logical_or(
        'Black Spruce Mixedwood', 'True Fir Mixedwood')))
    blackspruce = np.logical_and(sp == 'Black Spruce', sp == 'Black Spruce')
    blackspruce_wl = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland', sp == 'Larch Tamarack Wetland')
    blackspruce_larch = np.logical_or(sp == 'Black Spruce/Larch Tamarack Wetland',
                                      np.logical_or(sp == 'Larch Tamarack Wetland',
                                                    sp == 'Mixed Conifer (Larch Tamarack)'))
    industrial = np.logical_or(
        np.logical_or('Industrial Reclamation-Vegetated', 'Partial Cut/Regenerating Clearcut'),
        np.logical_or('Non-Veg ROWs', 'Herbaceous'))

    wetgraminiod = np.logical_or(np.logical_or('Bryophytic', 'Wet Graminoid'),
                                 np.logical_or('Grassland m', np.logical_or('Shrub Wetland', 'Grassland Mesic')))

    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), pine)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), whitespruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), m_blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), blackspruce_larch)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'd'), industrial)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), pine)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), whitespruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), m_blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), blackspruce_larch)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'm'), industrial)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), pine)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), whitespruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), m_blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), blackspruce_larch)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'd'), industrial)] = 'm'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), pine)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), whitespruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), m_blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), blackspruce_larch)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'm'), industrial)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), pine)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), whitespruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), m_blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), blackspruce_larch)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'L', mr == 'w'), industrial)] = 'l'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), pine)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), whitespruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_whitespruce)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), m_blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_wl)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), blackspruce_larch)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'd'), industrial)] = 'm'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), pine)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), whitespruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_whitespruce)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), m_blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_wl)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), blackspruce_larch)] = 'h'
    dn2[np.logical_and(np.logical_and(wet == 'wet area', mr == 'm'), industrial)] = 'h'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), pine)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), whitespruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_whitespruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), m_blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_wl)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), blackspruce_larch)] = 'l'
    dn2[np.logical_and(np.logical_and(reg == 'M', mr == 'w'), industrial)] = 'l'

    reduce(dn2)

def main():
    path=r"C:\SCARI\\"
    csvname = "Scari_DSS_2017_geoff.csv"
    outname="Scari_DSS_2017_geoff_clean.csv"

    csvfile=path+csvname
    outputfile=path+outname


    while not os.path.exists(csvfile):
        csvfile = raw_input("Input the name again: ")
    print("Start to process data: ", csvfile)

    avi = pd.read_csv(csvfile, sep=',', header=0, low_memory=False)
    #reg
    d_reg=avi['reg']
    d_mr=avi['MOIST_REG']
    d_sp=avi['SP1']
    d_wt=avi['MOISTURE1']

    avi['Treatment']=treat(d_reg,d_mr,d_sp,d_wt)
    avi['Density1'] = density1(d_reg, d_mr, d_sp, d_wt)
    avi['Planting'] = planting(d_reg, d_mr, d_sp, d_wt)
    avi['Density2'] = density2(d_reg, d_mr, d_sp, d_wt)

    avi.to_csv(outputfile, sep=',', index=False)


if __name__ == "__main__":

    main()
