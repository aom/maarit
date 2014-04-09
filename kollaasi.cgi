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

# listaus tiedoston luominen

require "/home/oranssi/public_html/maarit/core/muuttujat";

$tknimi = $IN{kuvat};
$mistamihin = $IN{nayta};

$title = "Kuvaluettelo [$tknimi].";
&PageHeader;
&PageFooter;
&PageTopic;

# haetaan: kollaasi.cgi?kuvat=kusti20&nayta=1-10

print $page_header;

print "<img src=\"core/navi_palkki.gif\" width=\"128\" height=\"25\" border=\"0\">";
print "<a href=\"kannat.shtml\"><img src=\"core/navi_index.gif\" width=\"20\" height=\"25\" border=\"0\" alt=\"Maaritin index...\"></a>\n";

# ensin tsekataan kuin monta tietuetta omistetaan

    if (open (KUVAREAD, "$laeskitdir/$tknimi/$tknimi.dat")) {
            flock (KUVAREAD, 2);
                @KuvaRead = <KUVAREAD>;
        close (KUVAREAD); }
    else {
        print "<p class=\"report2\">TIEDOSTO: $tknimi.dat :: virhe ($!)</p>\n"; }

foreach $line2 (@KuvaRead) {
    $kuvalkm++;
}

# sitten

if ( $mistamihin eq "" ) { $mistamihin = ("1-" . $kuvalkm); }

($mista, $mihin) =  split(/-/,$mistamihin);

$rivinvaihto = 1;
$rivinvaihto2 = 1;
$solunvari = "oranssi";

$mista--;

            print "<table width=\"600\" cellpadding=\"15\" cellspacing=\"0\" border=\"0\">\n";
            print "<tr>\n";
            print "<td width=\"100%\" align=\"left\" valign=\"top\">\n";

    print "<form method=\"post\" action=\"kollaasi.cgi\">\n";
    print "<input type=\"hidden\" name=\"kuvat\" value=\"$tknimi\">\n";
    print "<table width=\"600\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">\n";
    print " <tr>\n";
    print "  <td width=\"308\" height=\"30\" align=\"left\" valign=\"bottom\"><span class=\"normo\">Kuvia yhteens‰</span></td>\n";
    print "  <td width=\"160\" height=\"30\" align=\"right\" valign=\"bottom\"><span class=\"normo\"><b>$kuvalkm</b></span></td>\n";
    print " </tr>\n";
    print " <tr>\n";
    print "  <td width=\"308\" height=\"30\" align=\"left\" valign=\"bottom\"><span class=\"normo\">N‰ytet‰‰n kuvat</span></td>\n";
    print "  <td width=\"160\" height=\"30\" align=\"right\" valign=\"bottom\"><span class=\"normo\"><b>$mistamihin</b></span></td>\n";
    print " </tr>\n";
    print " <tr>\n";
    print "  <td width=\"308\" height=\"30\" align=\"left\" valign=\"bottom\"><span class=\"normo\">Mitk‰ kuvat n‰ytet‰‰n</span></td>\n";
    print "  <td width=\"160\" height=\"30\" align=\"right\" valign=\"bottom\"><font size=\"-1\" face=\"Verdana, Arial, Helvetica\"><input type=\"text\" name=\"nayta\" size=\"6\" value=\"x-y\"></font>&nbsp;&nbsp;<input type=\"image\" src=\"core/navi_nayta.gif\" name=\"submit\" width=\"50\" height=\"25\" border=\"0\" hspace=\"0\" vspace=\"0\" alt=\"N‰yt‰...\"></td>\n";
    print " </tr></form>\n";
    print " <tr>\n";
    print "  <td width=\"308\" height=\"30\" align=\"left\" valign=\"bottom\"><span class=\"normo\">Tai n‰yt‰ kaikki kuvat</span></td>\n";
    print "  <td width=\"160\" height=\"30\" align=\"right\" valign=\"bottom\"><a href=\"kollaasi.cgi?kuvat=$tknimi&nayta=1-$kuvalkm\"><img src=\"core/navi_nayta.gif\" width=\"50\" height=\"25\" border=\"0\" alt=\"N‰yt‰...\"></td>\n";
    print " </tr>\n";
    print "</table>\n";

    if (open (KUVADESC, "$laeskitdir/$tknimi/$tknimi.desc")) {
            flock (KUVADESC, 2);
                @KuvaDesc = <KUVADESC>;
        close (KUVADESC); }
    else {
        print "<p class=\"report2\">TIEDOSTO: $tknimi.desc :: virhe ($!)</p>\n"; }

   foreach $line (@KuvaDesc) {
        print $line; }


            print "</td>\n";
            print "</tr>\n";
            print "</table>\n";

    print "\n";

    print "<table width=\"600\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\"><tr><td bgcolor=\"#ffffff\"><table width=\"100%\" cellpadding=\"8\" cellspacing=\"2\" border=\"0\">\n";
#   print " <tr>\n";
#   print "  <td bgcolor=\"#007CAA\" align=\"left\"><img src=\"core/1pxl.gif\" width=\"100\" height=\"1\" border=\"0\"></td>\n";
#   print "  <td bgcolor=\"#007CAA\" align=\"left\"><img src=\"core/1pxl.gif\" width=\"100\" height=\"1\" border=\"0\"></td>\n";
#   print "  <td bgcolor=\"#007CAA\" align=\"left\"><img src=\"core/1pxl.gif\" width=\"100\" height=\"1\" border=\"0\"></td>\n";
#   print "  <td bgcolor=\"#007CAA\" align=\"left\"><img src=\"core/1pxl.gif\" width=\"100\" height=\"1\" border=\"0\"></td>\n";
#   print "  <td bgcolor=\"#007CAA\" align=\"left\"><img src=\"core/1pxl.gif\" width=\"100\" height=\"1\" border=\"0\"></td>\n";
#   print " </tr>\n";
    print " <tr>\n";

    for ( $tulostus = $mista; $tulostus < $mihin; $tulostus++ ) {
        ($kuvanumero, $kuvanimi, $osoite, $isokuva, $pikkukuva, $ikw, $ikh, $pkw, $pkh) =  split(/\|\|/,$KuvaRead[$tulostus]);
        if ( $rivinvaihto eq 1 && $rivinvaihto2 ne 1 ) {
            print " <tr>\n";
            $rivinvaihto2 = 0;
        }

        if ( $solunvari eq "oranssi" ) {
            print "  <td bgcolor=\"#FFA201\" align=\"center\" valign=\"middle\"><a href=\"$url/kuva.cgi?kuvat=$tknimi&kuva=$kuvanumero&nayta=$mistamihin\">";
            print "<img src=\"$osoite/peukalot/$pikkukuva\" width=\"$pkw\" height=\"$pkh\" border=\"0\" alt=\"$kuvanimi\"></a><br>\n";
            print "  <span class=\"kuvaseli\">$isokuva<br>$ikw x $ikh</span></td>\n";

            $solunvari = "punainen";
            if ( $rivinvaihto eq 5 ) {
                print " </tr>\n";
            	$rivinvaihto = 1;
            	next;
            }
            $rivinvaihto++;
        next;
        }
        if ( $solunvari eq "punainen" ) {
            print "  <td bgcolor=\"#FF7301\" align=\"center\" valign=\"middle\"><a href=\"$url/kuva.cgi?kuvat=$tknimi&kuva=$kuvanumero&nayta=$mistamihin\"><img src=\"$osoite/peukalot/$pikkukuva\" width=\"$pkw\" height=\"$pkh\" border=\"0\" alt=\"$kuvanimi\"></a><br>\n";
            print "  <span class=\"kuvaseli\">$isokuva<br>$ikw x $ikh</span></td>\n";

            $solunvari = "oranssi";
            if ( $rivinvaihto eq 5 ) {
                print " </tr>\n";
            	$rivinvaihto = 1;
            	next;
            }
            $rivinvaihto++;
        next;
        }
        else { print "<p>Virhe, jotain outoa on tekeill‰. haistatko sin‰kin rikin hajun?\n"; }
    }

# sitten tarkistetaan, jos j‰i tyhji‰ cellej‰ ja t‰ytet‰‰n ne...

    if ( $rivinvaihto eq 2 ) {
        print "  <td bgcolor=\"#505A64\" align=\"center\" valign=\"middle\"><img src=\"core/1pxl.gif\" width=\"1\" height=\"1\" border=\"0\"></td>\n";
        $rivinvaihto++;
    }
    if ( $rivinvaihto eq 3 ) {
        print "  <td bgcolor=\"#505A64\" align=\"center\" valign=\"middle\"><img src=\"core/1pxl.gif\" width=\"1\" height=\"1\" border=\"0\"></td>\n";
        $rivinvaihto++;
    }
    if ( $rivinvaihto eq 4 ) {
        print "  <td bgcolor=\"#505A64\" align=\"center\" valign=\"middle\"><img src=\"core/1pxl.gif\" width=\"1\" height=\"1\" border=\"0\"></td>\n";
        $rivinvaihto++;
    }
    if ( $rivinvaihto eq 5 ) {
        print "  <td bgcolor=\"#505A64\" align=\"center\" valign=\"middle\"><img src=\"core/1pxl.gif\" width=\"1\" height=\"1\" border=\"0\"></td>\n";
        print " </tr>\n";
    }

    print "</table></td></tr></table>\n";

print $page_footer;


# SUBs
#################################################