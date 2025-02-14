import uiautomator2 as u2


def get_all_elements_xpath():
    d = u2.connect()  # 连接到设备
    elements_xpath = []
    xml_source = d.dump_hierarchy()
    from lxml import etree
    root = etree.fromstring(xml_source.encode('utf-8'))

    def traverse(node, path):
        nonlocal elements_xpath
        current_path = path + "/" + node.tag
        elements_xpath.append(current_path)
        for child in node:
            traverse(child, current_path)

    traverse(root, "")
    return elements_xpath


if __name__ == "__main__":
    all_xpath = get_all_elements_xpath()
    for xpath in all_xpath:
        print(xpath)
