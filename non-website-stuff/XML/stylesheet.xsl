<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
    xmlns:t="http://www.tei-c.org/ns/1.0">
    <xsl:output method="html" indent="yes"/>

    <!-- General template to handle elements with a 'rend' attribute -->
    <xsl:template match="t:*[@rend]">
        <span>
            <xsl:attribute name="class">
                <xsl:value-of select="@rend"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <!-- General template to handle elements without HTML tags -->
    <xsl:template match="t:*[not(*) and not(@rend)]">
        <span class="{local-name()}">
            <xsl:value-of select="normalize-space()"/>
        </span>
    </xsl:template>

    <!-- Specific templates for orgName, persName, etc. -->
    <xsl:template match="t:orgName">
        <span class="{@type}">
            <xsl:if test="@rend">
                <xsl:attribute name="class">
                    <xsl:value-of select="@rend"/>
                </xsl:attribute>
            </xsl:if>
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="t:persName">
        <span class="{@type}">
            <xsl:if test="@rend">
                <xsl:attribute name="class">
                    <xsl:value-of select="@rend"/>
                </xsl:attribute>
            </xsl:if>
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <!-- Main template -->
    <xsl:template match="/t:TEI">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>The Guardian's Cover page on the fall of the Berlin Wall</title>
                <link rel="stylesheet" type="text/css" href="media/CSS/tei_styles.css"/>
            </head>
            <body>
                <xsl:apply-templates select="t:teiHeader"/>
                <xsl:apply-templates select="t:text"/>
            </body>
        </html>
    </xsl:template>

    <!-- Template for paragraph content excluding initial segment (headings etc.) -->
    <xsl:template match="t:p">
        <!-- Output the text of paragraphs, including nested elements like emph, name, persName, date, placeName etc. -->
        <p>
            <xsl:value-of select="normalize-space()"/>
        </p>
    </xsl:template>

</xsl:stylesheet>
