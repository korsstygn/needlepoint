<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>
                    <xsl:value-of select="//tei/tei:titleStmt/tei:title"/>
                </title>
                <!-- Add the CSS reference -->
                <xsl:element name="link">
                    <xsl:attribute name="rel">stylesheet</xsl:attribute>
                    <xsl:attribute name="type">text/css</xsl:attribute>
                    <xsl:attribute name="href">styles.css</xsl:attribute> <!-- Change 'styles.css' to your CSS file's path -->
                </xsl:element>
            </head>
            <body>
                <xsl:apply-templates select="tei:TEI/tei:text/tei:body"/>
            </body>
        </html>
    </xsl:template>

    <!-- The rest of your templates remain unchanged -->

    <xsl:template match="tei:body">
        <xsl:apply-templates select="tei:div"/>
    </xsl:template> 

    <xsl:template match="tei:div">
        <div>
            <xsl:apply-templates select="tei:head | tei:byline | tei:p | tei:figure | tei:list"/>
        </div>
    </xsl:template>

    <xsl:template match="tei:byline">
        <p>
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
</xsl:stylesheet>
