from generate_graph import GraphVizBuilder

ar6_wg1 = GraphVizBuilder("AR6_WGI", rankdir="TB")  # Use top-to-bottom layout

# Main Nodes (with light blue color)
ar6_wg1.add_node("AR6", "AR6 WGI", url="https://www.ipcc.ch/report/ar6/wg1/", color="lightblue")
ar6_wg1.add_node("SPM", "Summary for Policymakers", url="https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/")
ar6_wg1.add_node("TS", "Technical Summary", url="https://www.ipcc.ch/report/ar6/wg1/chapter/technical-summary/")
ar6_wg1.add_node("FR", "Full Report", url="https://www.ipcc.ch/report/ar6/wg1/")
ar6_wg1.add_node("CP", "Chapters", url="https://www.ipcc.ch/report/ar6/wg1/", color="lightyellow")  # Set a different color
ar6_wg1.add_node("FMI", "Front Matter, Annexes, and Index", url="https://www.ipcc.ch/report/ar6/wg1/", color="lightgrey")  # Add FMI section

# Sub-nodes of Chapters in WGI (with different color for sub-nodes)
for i in range(1, 13):
    ar6_wg1.add_node(f"CP{i}", f"Chapter {i}", url=f"https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-{i}/", color="lightcoral")  # Use light coral for chapters

# Sub-nodes of Cross-Chapters in WGII (with different color for sub-nodes)
#for i in range(1, 8):
    #ar6_wg1.add_node(f"CPP{i}", f"Cross-Chapter {i}", url=f"https://www.ipcc.ch/report/ar6/wg2/chapter/ccp{i}/", color="lightseagreen")  # Use light seagreen for cross-chapters

# Connect the main node (Chapters) to the sub-chapters
for i in range(1, 13):
    ar6_wg1.add_edge("CP", f"CP{i}")

# Connect "Front Matter, Annexes, and Index" to its subtopics
#for i in range(1, 13):
    #ar6_wg1.add_edge("FMI", f"FMI{i}")

# Connect the main nodes
ar6_wg1.add_edge("AR6", "SPM")
ar6_wg1.add_edge("AR6", "TS")
ar6_wg1.add_edge("AR6", "FR")
ar6_wg1.add_edge("AR6", "CP")
ar6_wg1.add_edge("AR6", "FMI")

# Adjusting graph attributes to provide more space
ar6_wg1.graph.attr(
    size="auto",        # Increase size to give more space
    rankdir="TB",        # Use top-to-bottom layout
    nodesep="1",         # Increase space between nodes
    ranksep="1",         # Increase space between ranks (levels)
    margin="0.5",        # Add margin around the graph to avoid tight borders
)

ar6_wg1.render_graph("ar6_wgi_summary", open_in_browser=True)

