<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
    xmlns:tei="http://www.tei-c.org/ns/1.0">
    <xsl:output method="xml" indent="yes" />

    <!-- Template to match the root TEI element -->
    <xsl:template match="/tei:TEI">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>The Guardian's Cover page on the fall of the Berlin Wall</title>
                <link rel="stylesheet" type="text/css" href="media/CSS/tei_styles.css" />
            </head>
            <body>
                <xsl:apply-templates select="tei:teiHeader" />
                <xsl:apply-templates select="tei:text" />
            </body>
        </html>
    </xsl:template>

    <!-- Header Information -->
    <xsl:template match="tei:teiHeader">
        <!-- Header Information -->
        <xsl:apply-templates select="tei:fileDesc" />
        <xsl:apply-templates select="tei:encodingDesc" />
    </xsl:template>

    <xsl:template match="tei:fileDesc">
        <h2>File Description</h2>
        <xsl:apply-templates select="tei:titleStmt" />
        <xsl:apply-templates select="tei:publicationStmt" />
        <xsl:apply-templates select="tei:sourceDesc" />
    </xsl:template>

    <xsl:template match="tei:titleStmt">
        <h3>Title Statement</h3>
        <p>Title: <xsl:value-of select="tei:title" />
        </p>
        <p>Author: <xsl:value-of select="tei:author" />
        </p>
        <xsl:apply-templates select="tei:respStmt" />
    </xsl:template>

    <xsl:template match="tei:respStmt">
        <p>Responsibility: <xsl:value-of select="tei:resp" />
, Name: <xsl:value-of select="tei:name" />
    </p>
</xsl:template>

<xsl:template match="tei:publicationStmt">
    <h3>Publication Statement</h3>
    <p>Publisher: <xsl:value-of select="tei:publisher" />
    </p>
    <p>Publication Place: <xsl:value-of select="tei:pubPlace" />
    </p>
    <p>Date: <xsl:value-of select="tei:date" />
    </p>
    <p>Availability: <xsl:value-of select="tei:availability" />
    </p>
</xsl:template>

<xsl:template match="tei:sourceDesc">
    <h3>Source Description</h3>
    <p>Source: <xsl:value-of select="." />
    </p>
</xsl:template>

<xsl:template match="tei:encodingDesc">
    <h3>Encoding Description</h3>
    <p>Editorial Declaration: <xsl:value-of select="tei:editorialDecl" />
    </p>
</xsl:template>




<!-- General template to handle elements without HTML tags -->
<xsl:template match="tei:*[not(*) and not(@rend)]">
    <span class="{local-name()}">
        <xsl:value-of select="normalize-space()"/>
    </span>
</xsl:template>

<!-- Specific templates for orgName, persName, etc. -->
<xsl:template match="tei:orgName">
    <span class="{@type}">
        <xsl:if test="@rend">
            <xsl:attribute name="class">
                <xsl:value-of select="@rend"/>
            </xsl:attribute>
        </xsl:if>
        <xsl:apply-templates/>
    </span>
</xsl:template>

<xsl:template match="tei:persName">
    <span class="{@type}">
        <xsl:if test="@rend">
            <xsl:attribute name="class">
                <xsl:value-of select="@rend"/>
            </xsl:attribute>
        </xsl:if>
        <xsl:apply-templates/>
    </span>
</xsl:template>




<!-- Template to match the text element -->
<xsl:template match="tei:text">
    <!-- Text Content -->
    <xsl:apply-templates select="tei:body" />
</xsl:template>

<xsl:template match="tei:body">
    <xsl:apply-templates select="*" />
</xsl:template>

<xsl:template match="tei:p">
    <p>
        <xsl:apply-templates select="*|text()" />
    </p>
</xsl:template>

<xsl:template match="tei:head">
    <span class="TEI_head">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:byline">
    <span class="byline">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:emph">
    <strong>
        <xsl:apply-templates select="*|text()" />
    </strong>
</xsl:template>

<xsl:template match="tei:hi">
    <span class="HI">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:measure">
    <span>
        <xsl:value-of select="@quantity" />
        <xsl:value-of select="@unit" />
    </span>
</xsl:template>

<xsl:template match="tei:date">
    <span class="tei-date">
        <xsl:value-of select="." />
    </span>
</xsl:template>

<xsl:template match="tei:placeName">
    <span class="tei-placeName">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<!-- <xsl:template match="tei:orgName">
        <span class="tei-orgName">
            <xsl:apply-templates select="*|text()" />
        </span>
    </xsl:template> -->

<xsl:template match="tei:nationality">
    <span class="tei-nationality">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:objectName">
    <span class="tei-objectName">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:glyph">
    <span class="tei-glyph" title="{ @desc }" />
</xsl:template>

<xsl:template match="tei:persName">
        <span class="tei-persName">
            <xsl:apply-templates select="*|text()" />
        </span>
    </xsl:template>

<xsl:template match="tei:roleName">
    <span class="tei-roleName">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template>

<xsl:template match="tei:quote">
    <blockquote>
        <xsl:apply-templates select="*|text()" />
    </blockquote>
</xsl:template>

<xsl:template match="tei:ref">
    <a href="{substring-after(@target, '#')}">
        <xsl:apply-templates select="*|text()" />
    </a>
</xsl:template>

<xsl:template match="tei:figure">
    <figure>
        <xsl:apply-templates select="tei:graphic" />
        <figcaption>
            <xsl:apply-templates select="tei:head" />
            <xsl:apply-templates select="tei:figDesc" />
            <p>PHOTOGRAPH: <xsl:apply-templates select="tei:persName" />
            </p>
        </figcaption>
    </figure>
</xsl:template>

<xsl:template match="tei:graphic">
    <img src="{@url}" alt="graphic" />
</xsl:template>

<!-- Template to extract the URL -->
<xsl:template mode="url" match="@url">
    <img src="{.}" />
</xsl:template>

<!-- <xsl:template match="placeName">
    <span class="tei-placeName">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template> -->

<xsl:template match="figDesc">
    <p class="TEI_figDesc">
        <xsl:value-of select="." />
    </p>
</xsl:template>

<!-- <xsl:template match="tei:persName">
    <span class="TEI_persName">
        <xsl:apply-templates select="forename" />
        <xsl:text></xsl:text>
        <xsl:apply-templates select="surname" />
    </span>
</xsl:template>

<xsl:template match="tei:forename">
    <span class="tei-foreName">
        <xsl:value-of select="." />
    </span>
</xsl:template>

<xsl:template match="tei:surname">
    <span class="tei-surname">
        <xsl:value-of select="." />
    </span>
</xsl:template> -->

<xsl:template match="tei:list">
    <ul>
        <xsl:apply-templates select="tei:item" />
    </ul>
</xsl:template>

<xsl:template match="tei:item">
    <li>
        <xsl:apply-templates select="*|text()" />
    </li>
</xsl:template>

<!-- <xsl:template match="tei:seg">
    <span id="{ @title }" class="tei-seg">
        <xsl:apply-templates select="*|text()" />
    </span>
</xsl:template> -->

<xsl:template match="tei:choice">
    <span class="tei-choice">
        <xsl:apply-templates select="tei:corr" />
    </span>
</xsl:template>

<xsl:template match="tei:hr">
    <hr />
</xsl:template>

<xsl:template match="tei:cb">
    <br />
</xsl:template>

<xsl:template match="tei:lb">
    //* In original <br />  *//
</xsl:template>
</xsl:stylesheet>
