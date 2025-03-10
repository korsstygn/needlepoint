<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>
                    <xsl:value-of select="//tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
                </title>
                <link rel="stylesheet" type="text/css" href="media/CSS/tei_styles.css"/> 
            </head>
            <body>
                <div class="container">
                    <xsl:apply-templates select="tei:TEI/tei:text/tei:body"/>
                </div>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="tei:body">
        <xsl:apply-templates select="tei:div"/>
    </xsl:template> 

    <xsl:template match="tei:div">
        <div class="article-container">
            <xsl:apply-templates select="tei:head | tei:byline | tei:p | tei:figure | tei:list"/>
        </div>
    </xsl:template>

    <xsl:template match="tei:head">
        <div class="headline-container">
            <span class="headline">
                <xsl:value-of select="."/>
            </span>
        </div>
    </xsl:template>

    <xsl:template match="tei:byline">
        <p class="byline">
            <em>
                <xsl:apply-templates/>
            </em>
        </p>
    </xsl:template>

    <xsl:template match="tei:p">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
        <xsl:template match="tei:lb">
        <br />
            <xsl:apply-templates/>
        
    </xsl:template>

    <xsl:template match="tei:figure">
        <div class="image-container">
            <img class="main-image" src="{@url}" alt="{@n}"/>
        </div>
    </xsl:template>

    <xsl:template match="tei:list">
        <ul>
            <xsl:apply-templates select="tei:item"/>
        </ul>
    </xsl:template>

    <xsl:template match="tei:item">
        <li>
            <xsl:apply-templates/>
        </li>
    </xsl:template>

    <xsl:template match="tei:placeName">
        <xsl:choose>
            <xsl:when test="tei:seg[@rend='initial']">
                <span style="font-size: 1.5em; font-weight: bold;">
                    <xsl:value-of select="tei:seg[@rend='initial']"/>
                </span>
                <xsl:value-of select="substring(., string-length(tei:seg[@rend='initial']) + 1)"/>
            </xsl:when>
            <xsl:otherwise>
                <span style="font-style: italic;">
                    <xsl:apply-templates/>
                </span>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="tei:persName">
        <span style="font-weight: bold;">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:orgName">
        <span style="font-weight: bold;">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:hi[@rend='italic']">
        <span style="font-style: italic;">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:head[@rend='bold']">
        <span style="font-weight: bold;">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <!-- New template for column structure -->
    <xsl:template match="tei:div[@type='columns']">
        <div class="columns-container">
            <xsl:for-each select="tei:div[@type='column']">
                <div class="column">
                    <xsl:apply-templates/>
                </div>
                <xsl:if test="position() != last()">
                    <div class="column-divider"></div>
                </xsl:if>
            </xsl:for-each>
        </div>
    </xsl:template>

    <!-- New template for ad container -->
    <xsl:template match="tei:div[@type='ad']">
        <div class="ad-container">
            <xsl:apply-templates/>
        </div>
    </xsl:template>

    <!-- New template for horizontal divider -->
    <xsl:template match="tei:div[@type='horizontal-divider']">
        <div class="horizontal-divider"></div>
    </xsl:template>
</xsl:stylesheet>
