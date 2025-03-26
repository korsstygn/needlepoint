# MULTIMODALITY PROJECT 
### Group 1 - accompanying notes

For this project, we chose to remediate the front page of the **10 November 1989 print edition of The Guardian newspaper.**
A scan of this front page is made available by The Guardian on its own site here: uploads.guim.co.uk/2019/10/28/10 Nov 89.jpg
`media/img/1o_Nov_89.jpg` In our project folder

Our project had not one but two aims:

1. **Remediation as critical digitization:** We set out to create a *digitized* version of the front page, producing a faithful and exhaustive representation of our artefact, which includes not only full text but also rich metadata, indexing, descriptive encoding and full bibliographical information. This, then, we believe, fulfils the brief of the multimodality group project.

   1. `index_FINAL_Group_1_TEI.html`
        The TEI-XML document converted to HTML using the Python script in `XML/render_to_HTML.py` and the XSLT in `XML/stylesheet.xsl` both located in the folder XML. The metadata model is in `Notes/Metadata Model.docx`
   2. `Machine_Generated_Rendition/index.html`
        A version focusing on mimicking the structure and appearance of the original. Grids were approximated and the layout was done in Adobe Indesign. Grids and zones in `Machine_Generated_Rendition/Grids_and_zones`

 !!! info
    **Please note:** As per our agreement with Anton and Jacob following our project seminar on 19 March 2025, we have completed semantic encoding with TEI-XML only for the banner, photograph, three main articles, and short news stories in the bottom left corner of the front page. As this semantic layer proved to be a very time-consuming task, we opted to focus only on the articles of topical relevance, i.e., the fall of the Berlin Wall. Semantic encoding thus ends **on line 375**.

2. **Remediation as re-enactment:** We asked ourselves what The Guardian could have looked like had the newspaper already had a digital edition and/or made use of the affordances of the digital medium in 1989. We decided to enhance the print edition with hyperlinks and the use of additional modalities (such as video), offering further contextualization of the news covered by the newspaper on that day. We propose that such a re-enactment of the print edition of the newspaper could be used for educational or LAM purposes, preserving but also enhancing the original artefact and its narrative, presenting novel ways for the newspaper archive and the history it records to reach new audiences.

    1. `index.html` The coding aims to mimic the paper version while adding the flexibility of hypertext. The picture has been replaced by a video of the event. Yellow areas are links. Yellow borders are present to show where in the text semantic encoding has been done, as a way to visualise the possibilities inherent in a body of text.

!!! info
    **Please note:** This was a monumental task, and we ran into time constraints and technical obstacles. This second remediation illustrates how a project to create an interactive born-digital "copy" based on a historical "original" could be approached.
