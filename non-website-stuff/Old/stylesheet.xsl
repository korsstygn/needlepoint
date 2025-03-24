<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
                xmlns:tei="http://www.tei-c.org/ns/1.0">
    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="/tei:TEI">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>The Guardian's Cover page on the fall of the Berlin Wall</title>
                <link rel="stylesheet" type="text/css" href="/non-website-stuff/media/CSS/tei_styles.css" />
            </head>
            <body>
                <xsl:apply-templates select="tei:teiHeader"/>
                <xsl:apply-templates select="tei:text"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="tei:teiHeader">
        <h1 xmlns="http://www.w3.org/1999/xhtml">Header Information</h1>
        <xsl:apply-templates select="tei:fileDesc"/>
        <xsl:apply-templates select="tei:encodingDesc"/>
    </xsl:template>

    <xsl:template match="tei:fileDesc">
        <h2 xmlns="http://www.w3.org/1999/xhtml">File Description</h2>
        <xsl:apply-templates select="tei:titleStmt"/>
        <xsl:apply-templates select="tei:publicationStmt"/>
        <xsl:apply-templates select="tei:sourceDesc"/>
    </xsl:template>

    <xsl:template match="tei:titleStmt">
        <h3 xmlns="http://www.w3.org/1999/xhtml">Title Statement</h3>
        <p xmlns="http://www.w3.org/1999/xhtml">Title: <xsl:value-of select="tei:title"/></p>
        <p xmlns="http://www.w3.org/1999/xhtml">Author: <xsl:value-of select="tei:author"/></p>
        <xsl:apply-templates select="tei:respStmt"/>
    </xsl:template>

    <xsl:template match="tei:respStmt">
        <p xmlns="http://www.w3.org/1999/xhtml">Responsibility: <xsl:value-of select="tei:resp"/>, Name: <xsl:value-of select="tei:name"/></p>
    </xsl:template>

    <xsl:template match="tei:publicationStmt">
        <h3 xmlns="http://www.w3.org/1999/xhtml">Publication Statement</h3>
        <p xmlns="http://www.w3.org/1999/xhtml">Publisher: <xsl:value-of select="tei:publisher"/></p>
        <p xmlns="http://www.w3.org/1999/xhtml">Publication Place: <xsl:value-of select="tei:pubPlace"/></p>
        <p xmlns="http://www.w3.org/1999/xhtml">Date: <xsl:value-of select="tei:date"/></p>
        <p xmlns="http://www.w3.org/1999/xhtml">Availability: <xsl:value-of select="tei:availability"/></p>
    </xsl:template>

    <xsl:template match="tei:sourceDesc">
        <h3 xmlns="http://www.w3.org/1999/xhtml">Source Description</h3>
        <p xmlns="http://www.w3.org/1999/xhtml">Source: <xsl:value-of select="."/></p>
    </xsl:template>

    <xsl:template match="tei:encodingDesc">
        <h3 xmlns="http://www.w3.org/1999/xhtml">Encoding Description</h3>
        <p xmlns="http://www.w3.org/1999/xhtml">Editorial Declaration: <xsl:value-of select="tei:editorialDecl"/></p>
    </xsl:template>

    <xsl:template match="tei:text">
        <h1 xmlns="http://www.w3.org/1999/xhtml">Text Content</h1>
        <xsl:apply-templates select="tei:body"/>
    </xsl:template>
    <xsl:template match="tei:body">
        <xsl:apply-templates select="*"/>
    </xsl:template>

    <xsl:template match="tei:p">
        <p xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </p>
    </xsl:template>

    <xsl:template match="tei:head">
        <h3 xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </h3>
    </xsl:template>

    <xsl:template match="tei:byline">
        <p xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </p>
    </xsl:template>

    <xsl:template match="tei:emph">
        <strong xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </strong>
    </xsl:template>

    <xsl:template match="tei:hi">
        <i xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </i>
    </xsl:template>

    <xsl:template match="tei:measure">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:value-of select="@quantity"/> <xsl:value-of select="@unit"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:date">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:value-of select="."/>
        </span>
    </xsl:template>

    <xsl:template match="tei:placeName">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:orgName">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:nationality">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:objectName">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:glyph">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:value-of select="@desc"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:persName">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:roleName">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:quote">
        <blockquote xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </blockquote>
    </xsl:template>

    <xsl:template match="tei:ref">
        <a xmlns="http://www.w3.org/1999/xhtml" href="{substring-after(@target, '#')}">
            <xsl:apply-templates select="*|text()"/>
        </a>
    </xsl:template>
    <xsl:template match="tei:figure">
        <figure xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="tei:graphic"/>
            <figcaption>
                <xsl:apply-templates select="tei:head"/>
                <xsl:apply-templates select="tei:figDesc"/>
                <p xmlns="http://www.w3.org/1999/xhtml">PHOTOGRAPH: <xsl:apply-templates select="tei:persName"/></p>
            </figcaption>
        </figure>
    </xsl:template>

    <xsl:template match="tei:graphic">
        <img xmlns="http://www.w3.org/1999/xhtml" src="{@url}" alt="graphic"/>
    </xsl:template>

    <xsl:template match="tei:list">
        <ul xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="tei:item"/>
        </ul>
    </xsl:template>

    <xsl:template match="tei:item">
        <li xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </li>
    </xsl:template>

    <xsl:template match="tei:seg">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="*|text()"/>
        </span>
    </xsl:template>
    
    <xsl:template match="tei:choice">
        <span xmlns="http://www.w3.org/1999/xhtml">
            <xsl:apply-templates select="tei:corr"/>
        </span>
    </xsl:template>

    <xsl:template match="tei:hr">
        <hr xmlns="http://www.w3.org/1999/xhtml"/>
    </xsl:template>

    <xsl:template match="tei:cb">
        <br xmlns="http://www.w3.org/1999/xhtml"/>
    </xsl:template>

    <xsl:template match="tei:lb">
        <br xmlns="http://www.w3.org/1999/xhtml"/>
    </xsl:template>
    </xsl:stylesheet> 