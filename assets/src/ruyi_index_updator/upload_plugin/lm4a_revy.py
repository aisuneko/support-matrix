# pylint: disable=import-outside-toplevel, missing-function-docstring
"""
Upload plugin for LM4A Revy
"""
from .prelude import *  # pylint: disable=wildcard-import, unused-wildcard-import

__version__ = "0.0.1"


class Lm4aRevy(UploadPluginBase):
    """
    Class for LM4A Revy plugin
    """

    import urllib
    import bs4

    @staticmethod
    def get_name() -> str:
        return "lm4a_revy"

    can_handle_tup = {
        "revyos-sipeed-lpi4a": ("sipeed_licheepi4a", "debian", "null"),
        "uboot-revyos-sipeed-lpi4a-16g": ("sipeed_licheepi4a", "debian", "null"),
        "uboot-revyos-sipeed-lpi4a-8g": ("sipeed_licheepi4a", "debian", "null"),
    }

    def can_handle(self, vinfo: VInfo) -> bool:
        if vinfo in self.can_handle_tup.values():
            return True
        return False

    def is_mapped_ruyi_index(self, vinfo: VInfo, index: str) -> bool:
        if index in self.can_handle_tup and self.can_handle_tup[index] == vinfo:
            return True
        return False

    def handle_version(self, vinfo: VInfo) -> str:
        # Wait for ruyi to give a more specific definition
        return f"0.{vinfo.version}.0"

    def handle_report(self, vinfo: VInfo,
                      index: str, last_index: list[BoardImages]) -> BoardImages:
        if index == "revyos-sipeed-lpi4a":
            return self.handle_report_image(vinfo, index, last_index)
        if index == "uboot-revyos-sipeed-lpi4a-8g":
            return self.handle_report_uboot_8g(vinfo, index, last_index)
        if index == "uboot-revyos-sipeed-lpi4a-16g":
            return self.handle_report_uboot_16g(vinfo, index, last_index)
        raise ValueError(f"Unknown index {index}")

    def handle_report_image(self, vinfo: VInfo,
                            index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index != "revyos-sipeed-lpi4a":
            return None
        base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{vinfo.version}/"
        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        root_dist = None
        boot_dist = None

        for link in soup.select(selector):
            if 'root-lpi4a' in link.contents[0]:
                root_url = self.urllib.parse.urljoin(
                    base_url, str(link["href"]))
                root_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                root_file = self.download_file(root_path, root_url)
                root_dist = self.gen_distfile(root_file, root_url)
            elif 'boot-lpi4a' in link.contents[0]:
                boot_url = self.urllib.parse.urljoin(
                    base_url, str(link["href"]))
                boot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                boot_file = self.download_file(boot_path, boot_url)
                boot_dist = self.gen_distfile(boot_file, boot_url)

        desc = f"RevyOS {vinfo.version} image for Sipeed LicheePi 4A"
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info.metadata.desc = desc
        res.info.distfiles = [root_dist, boot_dist]
        res.info.blob.distfiles = [
            root_dist.name,
            boot_dist.name
        ]
        res.info.provisionable.partition_map = {
            "boot": boot_dist.name[:-4],
            "root": root_dist.name[:-4]
        }
        return res

    def handle_report_uboot_8g(self, vinfo: VInfo,
                               index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index != "uboot-revyos-sipeed-lpi4a-8g":
            return None
        base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{vinfo.version}/"
        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        uboot_dist = None

        for link in soup.select(selector):
            if link.contents[0] == "u-boot-with-spl-lpi4a.bin":
                uboot_url = self.urllib.parse.urljoin(
                    base_url, str(link["href"]))
                uboot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                uboot_file = self.download_file(uboot_path, uboot_url)
                uboot_dist = self.gen_distfile(uboot_file, uboot_url)
                uboot_dist.name = f"u-boot-with-spl-lpi4a-8g.{vinfo.version}.bin"

        desc = f"U-Boot image for LicheePi 4A (8G RAM) and RevyOS {vinfo.version}"
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info.metadata.desc = desc
        res.info.distfiles = [uboot_dist]
        res.info.blob.distfiles = [
            uboot_dist.name
        ]
        res.info.provisionable.partition_map = {
            "uboot": uboot_dist.name
        }
        return res

    def handle_report_uboot_16g(self, vinfo: VInfo,
                                index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index != "uboot-revyos-sipeed-lpi4a-16g":
            return None
        base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{vinfo.version}/"
        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        uboot_dist = None

        for link in soup.select(selector):
            if 'u-boot' in link.contents[0]\
                    and '16g' in link.contents[0]:
                uboot_url = self.urllib.parse.urljoin(
                    base_url, str(link["href"]))
                uboot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                uboot_file = self.download_file(uboot_path, uboot_url)
                uboot_dist = self.gen_distfile(uboot_file, uboot_url)
                uboot_dist.name = f"u-boot-with-spl-lpi4a-16g.{vinfo.version}.bin"

        desc = f"U-Boot image for LicheePi 4A (16G RAM) and RevyOS {vinfo.version}"
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info.metadata.desc = desc
        res.info.distfiles = [uboot_dist]
        res.info.blob.distfiles = [
            uboot_dist.name
        ]
        res.info.provisionable.partition_map = {
            "uboot": uboot_dist.name
        }
        return res


def register() -> UploadPluginBase | None:
    """
    Register the plugin
    """
    return Lm4aRevy()