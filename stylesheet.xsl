<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0">
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
        <xsl:choose>
            <xsl:when test="@type='article'">
                <div class="article-container">
                    <xsl:apply-templates select="tei:head | tei:byline"/>
                    <div class="column">
                        <xsl:apply-templates select="tei:p | tei:cb"/>
                    </div>
                </div>
            </xsl:when>
            <xsl:when test="@type='columns'">
                <div class="article-container" style="grid-template-columns: repeat({@data-columns}, 1fr);">
                    <xsl:apply-templates select="tei:head | tei:byline"/>
                    <div class="columns-container">
                        <xsl:apply-templates select="tei:div[@type='column'] | tei:cb"/>
                    </div>
                </div>
            </xsl:when>
            <xsl:when test="@type='section'">
                <div class="section-container">
                    <xsl:apply-templates select="tei:head"/>
                    <xsl:apply-templates select="tei:div[@type='article' or @type='columns']"/>
                </div>
            </xsl:when>
            <xsl:when test="@type='advertisement'">
                <div class="advertisement-container">
                    <xsl:apply-templates/>
                </div>
            </xsl:when>
            <xsl:when test="@type='horizontal-divider'">
                <hr/>
            </xsl:when>
            <xsl:when test="@type='masthead'">
                <div class="masthead">
                    <xsl:apply-templates/>
                </div>
            </xsl:when>
            <xsl:when test="@type='ticker'">
                <div class="ticker">
                    <xsl:apply-templates/>
                </div>
            </xsl:when>
            <xsl:otherwise>
                <div>
                    <xsl:apply-templates/>
                </div>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="tei:div[@type='column']">
        <div class="column" style="grid-column: span {(@span)};">
            <xsl:apply-templates/>
        </div>
        <xsl:if test="position() != last()">
            <div class="column-divider"></div>
        </xsl:if>
    </xsl:template>

    <xsl:template match="tei:head">
        <div class="headline-container">
            <span class="headline">
                <xsl:value-of select="."/>
            </span>
        </div>
    </xsl:template>

    <xsl:template match="tei:byline">
        <div class="byline-container">
            <hr/>
            <p class="byline">
                <em>
                    <xsl:apply-templates/>
                </em>
            </p>
            <hr/>
        </div>
    </xsl:template>

    <xsl:template match="tei:cb">
        <div class="column-break"></div>
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

    <xsl:template match="tei:head[@rend='bold']">
        <span style="font-weight: bold;">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:head[@type='sub']">
        <div class="sub-headline-container">
            <span class="sub-headline">
                <xsl:value-of select="."/>
            </span>
        </div>
    </xsl:template>
</xsl:stylesheet>