import os
import time
import six.moves.urllib as urllib


cwd = os.path.realpath(os.path.dirname(__file__))

def getKernelNameFromURL(url):
    return url.split('/')[-1]

def getPathFromUrl(url):
    return os.path.join(cwd, getKernelNameFromURL(url))

def cleanupFile(path):
    if os.path.exists(path):
        os.remove(path)

class CassiniKernels(object):
    cassPck_url     = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/pck/cpck05Mar2004.tpc"
    cassSpk_url     = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/981005_PLTEPH-DE405S.bsp"
    satSpk_url      = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/020514_SE_SAT105.bsp"
    cassTourSpk_url = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/030201AP_SK_SM546_T45.bsp"
    cassFk_url      = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/fk/cas_v40.tf"
    cassCk_url      = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/ck/04135_04171pc_psiv2.bc"
    cassSclk_url    = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/sclk/cas00167.tsc"
    cassIk_url      = "https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/ik/cas_iss_v10.ti"
    cassPck         = getPathFromUrl(cassPck_url)
    cassSpk         = getPathFromUrl(cassSpk_url)
    satSpk          = getPathFromUrl(satSpk_url)
    cassTourSpk     = getPathFromUrl(cassTourSpk_url)
    cassFk          = getPathFromUrl(cassFk_url)
    cassCk          = getPathFromUrl(cassCk_url)
    cassSclk        = getPathFromUrl(cassSclk_url)
    cassIk          = getPathFromUrl(cassIk_url)

def cleanup_Cassini_Kernels():
    cleanupFile(CassiniKernels.cassPck)
    cleanupFile(CassiniKernels.cassSpk)
    cleanupFile(CassiniKernels.satSpk)
    cleanupFile(CassiniKernels.cassTourSpk)
    cleanupFile(CassiniKernels.cassFk)
    cleanupFile(CassiniKernels.cassCk)
    cleanupFile(CassiniKernels.cassSclk)
    cleanupFile(CassiniKernels.cassIk)


class MarsKernels(object):
    merExt10_url        = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mer1-m-spice-6-v1.0/mer1sp_1000/data/spk/mer1_surf_rover_ext10_v1.bsp"
    merExt11_url        = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mer1-m-spice-6-v1.0/mer1sp_1000/data/spk/mer1_surf_rover_ext11_v1.bsp"
    merIau2000_url      = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mer1-m-spice-6-v1.0/mer1sp_1000/data/spk/mer1_ls_040128_iau2000_v1.bsp"
    merFK_url           = "https://naif.jpl.nasa.gov/pub/naif/MER/kernels/fk/mer1_v10.tf"
    mroPspOne_url       = "https://naif.jpl.nasa.gov/pub/naif/MRO/kernels/spk/mro_psp1.bsp"
    mroPspTwentyTwo_url = "https://naif.jpl.nasa.gov/pub/naif/MRO/kernels/spk/mro_psp22.bsp"
    mgsSclk_url         = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mgs-m-spice-6-v1.0/mgsp_1000/data/sclk/mgs_sclkscet_00061.tsc"
    mgsPck_url          = "https://naif.jpl.nasa.gov/pub/naif/pds/data/ody-m-spice-6-v1.0/odsp_1000/data/pck/mars_iau2000_v0.tpc"
    mgsIk_url           = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mgs-m-spice-6-v1.0/mgsp_1000/data/ik/mgs_moc_v20.ti"
    mgsSpk_url          = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mgs-m-spice-6-v1.0/mgsp_1000/data/spk/mgs_ext26.bsp"
    mgsCk_url           = "https://naif.jpl.nasa.gov/pub/naif/pds/data/mgs-m-spice-6-v1.0/mgsp_1000/data/ck/mgs_sc_ext26.bc"
    merExt10            = getPathFromUrl(merExt10_url)
    merExt11            = getPathFromUrl(merExt11_url)
    merIau2000          = getPathFromUrl(merIau2000_url)
    merFK               = getPathFromUrl(merFK_url)
    mroPspOne           = getPathFromUrl(mroPspOne_url)
    mroPspTwentyTwo     = getPathFromUrl(mroPspTwentyTwo_url)
    mgsSclk             = getPathFromUrl(mgsSclk_url)
    mgsPck              = getPathFromUrl(mgsPck_url)
    mgsIk               = getPathFromUrl(mgsIk_url)
    mgsSpk              = getPathFromUrl(mgsSpk_url)
    mgsCk               = getPathFromUrl(mgsCk_url)

def cleanup_Mars_Kernels():
    cleanupFile(MarsKernels.merExt10)
    cleanupFile(MarsKernels.merExt11)
    cleanupFile(MarsKernels.merIau2000)
    cleanupFile(MarsKernels.merFK)
    cleanupFile(MarsKernels.mroPspOne)
    cleanupFile(MarsKernels.mroPspTwentyTwo)
    cleanupFile(MarsKernels.mgsSclk)
    cleanupFile(MarsKernels.mgsPck)
    cleanupFile(MarsKernels.mgsIk)
    cleanupFile(MarsKernels.mgsSpk)
    cleanupFile(MarsKernels.mgsCk)


class ExtraKernels(object):
    voyagerSclk_url     = "http://naif.jpl.nasa.gov/pub/naif/VOYAGER/kernels/sclk/vg200022.tsc"
    earthTopoTf_url     = "http://naif.jpl.nasa.gov/pub/naif/generic_kernels/fk/stations/earth_topo_050714.tf"
    earthStnSpk_url     = "http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/stations/earthstns_itrf93_050714.bsp"
    earthGenPck_url     = "http://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/earth_720101_070426.bpc"
    earthHighPerPck_url = "http://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/earth_latest_high_prec.bpc"
    voyagerSclk         = getPathFromUrl(voyagerSclk_url)
    earthTopoTf         = getPathFromUrl(earthTopoTf_url)
    earthStnSpk         = getPathFromUrl(earthStnSpk_url)
    earthGenPck         = getPathFromUrl(earthGenPck_url)
    earthHighPerPck     = getPathFromUrl(earthHighPerPck_url)

def cleanup_Extra_Kernels():
    cleanupFile(ExtraKernels.voyagerSclk)
    cleanupFile(ExtraKernels.earthTopoTf)
    cleanupFile(ExtraKernels.earthStnSpk)
    cleanupFile(ExtraKernels.earthGenPck)
    cleanupFile(ExtraKernels.earthHighPerPck)


class CoreKernels(object):
    # note this gets updated
    currentLSK = 'naif0012.tls'
    #
    pck_url    = 'http://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc'
    spk_url    = 'http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de421.bsp'
    gm_pck_url = 'http://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/gm_de431.tpc'
    lsk_url    = 'http://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/{}'.format(currentLSK)
    pck        = getPathFromUrl(pck_url)
    spk        = getPathFromUrl(spk_url)
    gm_pck     = getPathFromUrl(gm_pck_url)
    lsk        = getPathFromUrl(lsk_url)
    standardKernelList = [pck, spk, gm_pck, lsk]
    testMetaKernel     = os.path.join(cwd, "exampleKernels.txt")

def cleanup_Core_Kernels():
    cleanupFile(CoreKernels.pck)
    cleanupFile(CoreKernels.spk)
    cleanupFile(CoreKernels.gm_pck)
    cleanupFile(CoreKernels.lsk)



def getKernel(url):
    kernelName = getKernelNameFromURL(url)
    kernelFile = os.path.join(cwd, kernelName)
    # does not download if files are present, which allows us to potentially cache kernels
    if not os.path.isfile(kernelFile):
        attemptDownload(url, kernelName, kernelFile, 5)


def attemptDownload(url, kernelName, targetFileName, num_attempts):
    current_attempt = 0
    while current_attempt < num_attempts:
        try:
            print("Attempting to Download kernel: {}".format(kernelName))
            current_kernel = urllib.request.urlopen(url, timeout=10)
            with open(targetFileName, "wb") as kernel:
                kernel.write(current_kernel.read())
            print("Downloaded kernel: {}".format(kernelName))
            break
        except urllib.error.URLError:
            print("Download of kernel: {} failed with URLError, trying agian after a bit.".format(kernelName))
        except urllib.error.HTTPError as h:
            print("Some http error when downloading kernel {}, error: ".format(kernelName), h, ", trying agian after a bit.")
        current_attempt += 1
        print("\t Attempting to Download kernel again...")
        time.sleep(2 + current_attempt)
    if current_attempt >= num_attempts:
        raise BaseException("Error Downloading kernel: {}, check if kernel exists at url: {}".format(kernelName, url))



def getStandardKernels():
    print("\tChecking for kernels...\n")
    getKernel(CoreKernels.pck_url)
    getKernel(CoreKernels.spk_url)
    getKernel(CoreKernels.gm_pck_url)
    getKernel(CoreKernels.lsk_url)


def getExtraTestKernels():
    # these are test kernels not included in the standard meta kernel
    getKernel(ExtraKernels.voyagerSclk_url)
    getKernel(ExtraKernels.earthTopoTf_url)
    getKernel(ExtraKernels.earthStnSpk_url)
    getKernel(ExtraKernels.earthGenPck_url)
    getKernel(ExtraKernels.earthHighPerPck_url)

def getExtraMarsTestKernels():
    getKernel(MarsKernels.merExt10_url)
    getKernel(MarsKernels.merExt11_url)
    getKernel(MarsKernels.merIau2000_url)
    getKernel(MarsKernels.merFK_url)
    print("About to Download 'mro_psp1.bsp' which is over 170MB...")
    getKernel(MarsKernels.mroPspOne_url)
    print("About to Download 'mro_psp22.bsp' which is over 105MB...")
    getKernel(MarsKernels.mroPspTwentyTwo_url)

def getMGSTestKernels():
    getKernel(MarsKernels.mgsSclk_url)
    getKernel(MarsKernels.mgsPck_url)
    getKernel(MarsKernels.mgsIk_url)
    getKernel(MarsKernels.mgsSpk_url)
    getKernel(MarsKernels.mgsCk_url)

def getCassiniTestKernels():
    getKernel(CassiniKernels.cassPck_url)
    getKernel(CassiniKernels.cassSpk_url)
    getKernel(CassiniKernels.satSpk_url)
    getKernel(CassiniKernels.cassTourSpk_url)
    getKernel(CassiniKernels.cassFk_url)
    getKernel(CassiniKernels.cassCk_url)
    getKernel(CassiniKernels.cassSclk_url)
    getKernel(CassiniKernels.cassIk_url)

def writeTestMetaKernel():
    # Update the paths!
    with open(os.path.join(cwd, "exampleKernels.txt"), 'w') as kernelFile:
        kernelFile.write('\\begindata\n')
        kernelFile.write('KERNELS_TO_LOAD = (\n')
        for kernel in CoreKernels.standardKernelList:
            kernelFile.write('\'{0}\'\n'.format(os.path.join(cwd, kernel)))
        kernelFile.write(')\n')
        kernelFile.write('\\begintext')
        kernelFile.close()
    print('\nDone writing test meta kernel.')


def downloadKernels():
    # Download the kernels listed in kernelList and kernelURLlist
    getStandardKernels()
    # Now grab any extra test kernels we need
    getExtraTestKernels()
    # Now create the meta kernel file for tests
    writeTestMetaKernel()
    # Now download other extra kernels
    getExtraMarsTestKernels()
    getMGSTestKernels()
    getCassiniTestKernels()


if __name__ == '__main__':
    downloadKernels()
