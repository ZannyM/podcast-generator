import yaml
import xml.etree.ElementTree as xml_tree
import os

# Ensure output directory exists
output_dir = "/app/output/"
os.makedirs(output_dir, exist_ok=True)

with open('/app/input/feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:googleplay': 'http://www.google.com/schemas/play-podcasts/1.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:atom': 'http://www.w3.org/2005/Atom',
    'xmlns:rawvoice': 'http://www.rawvoice.com/rawvoiceRssModule/',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
   
    xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })

# Save the XML file in /app/output/
output_path = os.path.join(output_dir, "podcast.xml")
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write(output_path, encoding='UTF-8', xml_declaration=True)

print(f"Podcast feed saved to {output_path}")
