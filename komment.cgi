#!/usr/bin/perl

# a photo gallery script by aom [mika@marttila.net] (c)2001

  # a komment sub-routine

# first things first

read(STDIN, $in, $ENV{'CONTENT_LENGTH'});
      $in = $ENV{'QUERY_STRING'} if $ENV{'QUERY_STRING'};
      @pairs = split(/&/, $in);
      foreach $pair (@pairs) {
             ($name, $value) = split(/=/, $pair);
             $value =~ tr/+/ /;
             $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
             $IN{$name} = $value;
      }

use CGI;
print CGI::header('text/html'),

$emptyvar = "";

#################################################
#
# the main program
#
#################################################

require "/home/oranssi/public_html/maarit/core/muuttujat";

$title = "Kuvan kommentointi.";
&PageHeader;
&PageFooter;

$inkommentti = $IN{komment};
$inkommenttinick = $IN{kommentnick};
$hakemistossa = $IN{hakemistossa};
$kuvanimi = $IN{kuvanimi};
$kuvakokoelma = $IN{kuvakokoelma};
$linkki = $IN{linkki};
$linkki2 = $IN{linkki2};

print $page_header;

print "<img src=\"core/navi_palkki.gif\" width=\"128\" height=\"25\" border=\"0\">";
print "<a href=\"kannat.shtml\"><img src=\"core/navi_index.gif\" width=\"20\" height=\"25\" border=\"0\" alt=\"Maaritin index...\"></a>";
print "<a href=\"$linkki2\"><img src=\"core/navi_galleria.gif\" width=\"19\" height=\"25\" border=\"0\" alt=\"Kuvaluetteloon...\"></a>";
print "<a href=\"$linkki\"><img src=\"core/navi_kuva.gif\" width=\"19\" height=\"25\" border=\"0\" alt=\"Kuvaluetteloon...\"></a>";

            print "<table width=\"600\" cellpadding=\"15\" cellspacing=\"0\" border=\"0\">\n";
            print "<tr>\n";
            print "<td width=\"100%\" align=\"left\" valign=\"top\">\n";

    if (open (KOMMENTDB, ">>$laeskitdir/$kuvakokoelma/$kuvanimi.komment")) {
        flock (KOMMENTDB, 2);
            print KOMMENTDB "<li><span class=\"norm\">$inkommentti // <b>$inkommenttinick</b></span>\n";
            print "<h1>Kommentointi onnistui!</h1>\n";
            print "<p>Kommentoit seuraavaa: $inkommentti<br>\n";
            print "Käytit nimimerkkiä: $inkommenttinick</p>\n";
        close (KOMMENTDB); }
    else {
        print "<h1>Kommentointi epäonnistui!</h1>\n"; }

            print "</td>\n";
            print "</tr>\n";
            print "</table>\n";

print $page_footer;
