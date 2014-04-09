#!/usr/bin/perl

# a photo gallery script by aom [mika@marttila.net] (c)2001

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

$title = "Kuva ja kommentit.";
$topic_title = "KOMMENTIT JA KOMMENTOINTI";
&PageHeader;
&PageFooter;
&PageTopic;

$kuvakokoelma = $IN{kuvat};
$kuva = $IN{kuva};
$mistamihin = $IN{nayta};

# haetaan: kuva.cgi?kuvat=aom1&kuva=Image001

print $page_header;

print "<img src=\"core/navi_palkki.gif\" width=\"128\" height=\"25\" border=\"0\">";
print "<a href=\"kannat.shtml\"><img src=\"core/navi_index.gif\" width=\"20\" height=\"25\" border=\"0\" alt=\"Maaritin index...\"></a>";
print "<a href=\"kollaasi.cgi?kuvat=$kuvakokoelma&nayta=$mistamihin\"><img src=\"core/navi_galleria.gif\" width=\"19\" height=\"25\" border=\"0\" alt=\"Kuvaluetteloon...\"></a>";

    if (open (KUVADB, "$laeskitdir/$kuvakokoelma/$kuvakokoelma.dat")) {
            flock (KUVADB, 2);
                @KuvaDB = <KUVADB>;
        close (KUVADB); }
    else {
        print "<p>Tietoa ei löydetty. ($kuvakokoelma.dat, $!)</p>\n"; }

    foreach $line (@KuvaDB) {
        chomp ($line);
        ($kuvanumero, $kuvanimi, $hakemisto, $isokuva, $pikkukuva, $ikw, $ikh, $pkw, $pkh) =  split(/\|\|/,$line);

        if ( "$kuvanumero" eq "$kuva" ) {
            $hakemistossa = $hakemisto;

$kuvalkm = $#KuvaDB;
$kuvalkm++;
$kuvanumero_edell = $kuvanumero;
$kuvanumero_seur = $kuvanumero;
$kuvanumero_edell--;
$kuvanumero_seur++;

            if ( $kuvanumero == 1 ) { }
            else { print "<a href=\"kuva.cgi?kuvat=$kuvakokoelma&kuva=$kuvanumero_edell&nayta=$mistamihin\"><img src=\"core/navi_edellinen.gif\" width=\"19\" height=\"25\" border=\"0\" alt=\"Edellinen kuva...\"></a>"; }
            if ( $kuvanumero == $kuvalkm ) { }
            else { print "<a href=\"kuva.cgi?kuvat=$kuvakokoelma&kuva=$kuvanumero_seur&nayta=$mistamihin\"><img src=\"core/navi_seuraava.gif\" width=\"19\" height=\"25\" border=\"0\" alt=\"Seuraava kuva...\"></a>\n"; }

            print "<table width=\"600\" cellpadding=\"15\" cellspacing=\"0\" border=\"0\">\n";
            print "<tr>\n";
            print "<td width=\"100%\" align=\"left\" valign=\"top\">\n";

            print "<img src=\"$hakemisto/$isokuva\" width=\"$ikw\" height=\"$ikh\" border=\"0\">\n";

            print "</td>\n";
            print "</tr>\n";
            print "</table>\n";

print $page_topic;

            print "<table width=\"600\" cellpadding=\"15\" cellspacing=\"0\" border=\"0\">\n";
            print "<tr>\n";
            print "<td width=\"100%\" align=\"left\" valign=\"top\">\n";

            print "<menu>\n";

            if (open (KOMMENTDB, "$laeskitdir/$kuvakokoelma/$kuvanimi.komment")) {
                flock (KOMMENTDB, 2);
                    @KommentDB = <KOMMENTDB>;
            close (KOMMENTDB); }
            else {
                print "<li><span class=\"norm\">ainoatakaan kommenttia vielä...</span>\n"; }

            foreach $line (@KommentDB) {
                print $line; }

            print "</menu>\n\n";

            print "<form method=\"post\" action=\"$url/komment.cgi\">\n";
            print "<input type=\"hidden\" name=\"linkki\" value=\"kuva.cgi?kuvat=$kuvakokoelma&kuva=$kuva&nayta=$mistamihin\">\n";
            print "<input type=\"hidden\" name=\"linkki2\" value=\"kollaasi.cgi?kuvat=$kuvakokoelma&nayta=$mistamihin\">\n";
            print "<input type=\"hidden\" name=\"kuvanimi\" value=\"$kuvanimi\">\n";
            print "<input type=\"hidden\" name=\"kuvakokoelma\" value=\"$kuvakokoelma\">\n";
            print "<input type=\"hidden\" name=\"hakemistossa\" value=\"$hakemistossa\">\n";
            print "<p><input type=\"text\" name=\"komment\" size=\"40\" value=\"kommentit\">&nbsp;\n";
            print "<input type=\"text\" name=\"kommentnick\" size=\"10\" value=\"nimimerkki\">&nbsp;\n";
            print "<input type=\"submit\" value=\"send\" name=\"submit\"></p>\n";

            print "</td>\n";
            print "</tr>\n";
            print "</table>\n";
        }
    }

print $page_footer;

# SUBs
#################################################