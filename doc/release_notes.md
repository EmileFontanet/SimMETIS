# 0.1 (October 2018)

- first release of SimMETIS (based on SimCADO)
- simulates all L,M and N band imaging modes of METIS (Q band may be supported later, if required)
- background values and zeropoints have been compared to back-of-the-envelope calculations and the METIS fluxes document E-TNT-MPIA-MET-1004 (by Roy van Boekel)
- the input data format can be any Source object that simcado understands (see documentation there), e.g. a point source, list of point sources, or an arbitrary FITS file
- the output data format corresponds to a finally calibrated, background-subtracted, science-grade data product. It includes noise from the background and the object itself (photon shot noise) as well as from the background subtraction process. Detector read noise is not included as it is always less 10% of the background noise for reasonable DITs in all filters. Detector dark current is irrelevant for all bands.
- emission from the entrance window (relevant in the N and Q bands) is included as a fudge factor (10% of the telescope background in N band).
- ELFN can be simulated in the N band by using the function that is supplied in the N band notebook.