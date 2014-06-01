from multiboot.patchinfo import PatchInfo
import multiboot.autopatcher as autopatcher

patchinfo = PatchInfo()

patchinfo.matches        = r"^Helly?(bean|kat)-.*\.zip$"
patchinfo.name           = 'HellyBean/HellyKat'
patchinfo.ramdisk        = 'jflte/AOSP/AOSP.def'
patchinfo.patch          = autopatcher.auto_patch
patchinfo.extract        = autopatcher.files_to_auto_patch
patchinfo.device_check   = False
