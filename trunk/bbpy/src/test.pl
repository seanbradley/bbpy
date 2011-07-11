
## Magic Inline Python. This will expose the ContextWS object.
## This is all you need to add or update a user.
## If you need to use other objects from the VO namespace that should also be possible.
use Inline Python => 'from BbPy.ContextWS import ContextWS';

## Now you can use this object like a normal Perl object.
## I will make sure there is good documentation, but the python should be easy enough to figure out.
my $context = new ContextWS;

## This is a proxy tool login. If you need to generate a new loginTool see ContextWS.registerTool
$context->loginTool("NAU","PythonFeed","*****") or die "Could not login to Web Service";

## Now we can get the userws or the coursews. Other available soon!
my $userws = $context->getUserWS();

## This is a simple helper method to add a user. It may work for updates, but since updates
## are broken for the current release of BB9.1, I have no idea! ;-)
## It should return an array of userid's that are created.
@insRoles = ("Student","Former Student","Faculty")
@out = $userws->createSimpleUser(true,"uid-from-perl",123456,"perl\@python.com","familyName","givenName");

print @out;
