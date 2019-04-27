PYTHON(1)                                                    General Commands Manual                                                   PYTHON(1)

NNAAMMEE
       python - an interpreted, interactive, object-oriented programming language

SSYYNNOOPPSSIISS
       ppyytthhoonn [ --BB ] [ --dd ] [ --EE ] [ --hh ] [ --ii ] [ --mm _m_o_d_u_l_e_-_n_a_m_e ]
              [ --OO ] [ --OOOO ] [ --RR ] [ --QQ _a_r_g_u_m_e_n_t ] [ --ss ] [ --SS ] [ --tt ] [ --uu ]
              [ --vv ] [ --VV ] [ --WW _a_r_g_u_m_e_n_t ] [ --xx ] [ --33 ] [ --??  ]
              [ --cc _c_o_m_m_a_n_d | _s_c_r_i_p_t | - ] [ _a_r_g_u_m_e_n_t_s ]

DDEESSCCRRIIPPTTIIOONN
       Python  is  an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax.  For
       an introduction to programming in Python, see the Python Tutorial.  The Python Library Reference documents built-in and  standard  types,
       constants,  functions and modules.  Finally, the Python Reference Manual describes the syntax and semantics of the core language in (per‐
       haps too) much detail.  (These documents may be located via the IINNTTEERRNNEETT RREESSOOUURRCCEESS below; they may be installed on your system as well.)

       Python's basic power can be extended with your own modules written in C or C++.  On most systems such modules may be dynamically  loaded.
       Python is also adaptable as an extension language for existing applications.  See the internal documentation for hints.

       Documentation for installed Python modules and packages can be viewed by running the ppyyddoocc program.

CCOOMMMMAANNDD LLIINNEE OOPPTTIIOONNSS
       --BB     Don't write _._p_y_[_c_o_] files on import. See also PYTHONDONTWRITEBYTECODE.

       --cc _c_o_m_m_a_n_d
              Specify  the command to execute (see next section).  This terminates the option list (following options are passed as arguments to
              the command).

       --dd     Turn on parser debugging output (for wizards only, depending on compilation options).

       --EE     Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.

       --hh ,,  --?? ,,  ----hheellpp
              Prints the usage for the interpreter executable and exits.

       --ii     When a script is passed as first argument or the --cc option is used, enter interactive mode after executing the script or the  com‐
              mand.   It  does  not read the $PYTHONSTARTUP file.  This can be useful to inspect global variables or a stack trace when a script
              raises an exception.

       --mm _m_o_d_u_l_e_-_n_a_m_e
              Searches _s_y_s_._p_a_t_h for the named module and runs the corresponding _._p_y file as a script.

       --OO     Turn on basic optimizations.  This changes the filename extension for compiled (bytecode) files from _._p_y_c to _._p_y_o.   Given  twice,
              causes docstrings to be discarded.

       --OOOO    Discard docstrings in addition to the --OO optimizations.

       --RR     Turn  on  "hash  randomization",  so  that the hash() values of str, bytes and datetime objects are "salted" with an unpredictable
              pseudo-random value.  Although they remain constant within an individual Python process, they are not predictable between repeated
              invocations of Python.

              This  is  intended to provide protection against a denial of service caused by carefully-chosen inputs that exploit the worst case
              performance of a dict construction, O(n^2) complexity.  See http://www.ocert.org/advisories/ocert-2011-003.html for details.

       --QQ _a_r_g_u_m_e_n_t
              Division control; see PEP 238.  The argument must be one of "old" (the default, int/int and long/long  return  an  int  or  long),
              "new"  (new  division  semantics,  i.e.  int/int and long/long returns a float), "warn" (old division semantics with a warning for
              int/int and long/long), or "warnall" (old division semantics with a warning for all use of the division operator).  For a  use  of
              "warnall", see the Tools/scripts/fixdiv.py script.

       --ss     Don't add user site directory to sys.path.

       --SS     Disable the import of the module _s_i_t_e and the site-dependent manipulations of _s_y_s_._p_a_t_h that it entails.

       --tt     Issue  a  warning when a source file mixes tabs and spaces for indentation in a way that makes it depend on the worth of a tab ex‐
              pressed in spaces.  Issue an error when the option is given twice.

       --uu     Force stdin, stdout and stderr to be totally unbuffered.  On systems where it matters, also put stdin, stdout and stderr in binary
              mode.   Note  that  there  is  internal buffering in xreadlines(), readlines() and file-object iterators ("for line in sys.stdin")
              which is not influenced by this option.  To work around this, you will want to use  "sys.stdin.readline()"  inside  a  "while  1:"
              loop.

       --vv     Print  a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded.  When
              given twice, print a message for each file that is checked for when searching for a module.  Also provides information  on  module
              cleanup at exit.

       --VV ,,  ----vveerrssiioonn
              Prints the Python version number of the executable and exits.

       --WW _a_r_g_u_m_e_n_t
              Warning  control.   Python  sometimes  prints  warning  message  to _s_y_s_._s_t_d_e_r_r.  A typical warning message has the following form:
              _f_i_l_e::_l_i_n_e:: _c_a_t_e_g_o_r_y:: _m_e_s_s_a_g_e_.  By default, each warning is printed once for each source line where it occurs.   This  option  con‐
              trols  how  often warnings are printed.  Multiple --WW options may be given; when a warning matches more than one option, the action
              for the last matching option is performed.  Invalid --WW options are ignored (a warning message is  printed  about  invalid  options
              when the first warning is issued).  Warnings can also be controlled from within a Python program using the _w_a_r_n_i_n_g_s module.

              The  simplest  form  of _a_r_g_u_m_e_n_t is one of the following _a_c_t_i_o_n strings (or a unique abbreviation): iiggnnoorree to ignore all warnings;
              ddeeffaauulltt to explicitly request the default behavior (printing each warning once per source line); aallll to print a warning each  time
              it  occurs (this may generate many messages if a warning is triggered repeatedly for the same source line, such as inside a loop);
              mmoodduullee to print each warning only the first time it occurs in each module; oonnccee to print each warning only the first time  it  oc‐
              curs in the program; or eerrrroorr to raise an exception instead of printing a warning message.

              The full form of _a_r_g_u_m_e_n_t is _a_c_t_i_o_n::_m_e_s_s_a_g_e::_c_a_t_e_g_o_r_y::_m_o_d_u_l_e::_l_i_n_e_.  Here, _a_c_t_i_o_n is as explained above but only applies to messages
              that match the remaining fields.  Empty fields match all values; trailing empty fields may be omitted.  The _m_e_s_s_a_g_e field  matches
              the  start of the warning message printed; this match is case-insensitive.  The _c_a_t_e_g_o_r_y field matches the warning category.  This
              must be a class name; the match test whether the actual warning category of the message is a subclass  of  the  specified  warning
              category.  The full class name must be given.  The _m_o_d_u_l_e field matches the (fully-qualified) module name; this match is case-sen‐
              sitive.  The _l_i_n_e field matches the line number, where zero matches all line numbers and is thus equivalent  to  an  omitted  line
              number.

       --xx     Skip  the  first  line of the source.  This is intended for a DOS specific hack only.  Warning: the line numbers in error messages
              will be off by one!

       --33     Warn about Python 3.x incompatibilities that 2to3 cannot trivially fix.

IINNTTEERRPPRREETTEERR IINNTTEERRFFAACCEE
       The interpreter interface resembles that of the UNIX shell: when called with standard input connected to a tty  device,  it  prompts  for
       commands and executes them until an EOF is read; when called with a file name argument or with a file as standard input, it reads and ex‐
       ecutes a _s_c_r_i_p_t from that file; when called with --cc _c_o_m_m_a_n_d, it executes the Python statement(s) given as _c_o_m_m_a_n_d.  Here _c_o_m_m_a_n_d may con‐
       tain  multiple  statements  separated by newlines.  Leading whitespace is significant in Python statements!  In non-interactive mode, the
       entire input is parsed before it is executed.

       If available, the script name and additional arguments thereafter are passed to the script in the Python variable _s_y_s_._a_r_g_v,  which  is  a
       list  of  strings (you must first _i_m_p_o_r_t _s_y_s to be able to access it).  If no script name is given, _s_y_s_._a_r_g_v_[_0_] is an empty string; if --cc
       is used, _s_y_s_._a_r_g_v_[_0_] contains the string _'_-_c_'_.  Note that options interpreted  by  the  Python  interpreter  itself  are  not  placed  in
       _s_y_s_._a_r_g_v.

       In interactive mode, the primary prompt is `>>>'; the second prompt (which appears when a command is not complete) is `...'.  The prompts
       can be changed by assignment to _s_y_s_._p_s_1 or _s_y_s_._p_s_2.  The interpreter quits when it reads an EOF at a prompt.  When an unhandled exception
       occurs, a stack trace is printed and control returns to the primary prompt; in non-interactive mode, the interpreter exits after printing
       the stack trace.  The interrupt signal raises the _K_e_y_b_o_a_r_d_I_n_t_e_r_r_u_p_t exception; other UNIX signals are not caught (except that SIGPIPE  is
       sometimes ignored, in favor of the _I_O_E_r_r_o_r exception).  Error messages are written to stderr.

FFIILLEESS AANNDD DDIIRREECCTTOORRIIEESS
       These  are subject to difference depending on local installation conventions; ${prefix} and ${exec_prefix} are installation-dependent and
       should be interpreted as for GNU software; they may be the same.  On Debian GNU/{Hurd,Linux} the default for both is _/_u_s_r.

       _$_{_e_x_e_c___p_r_e_f_i_x_}_/_b_i_n_/_p_y_t_h_o_n
              Recommended location of the interpreter.

       _$_{_p_r_e_f_i_x_}_/_l_i_b_/_p_y_t_h_o_n_<_v_e_r_s_i_o_n_>
       _$_{_e_x_e_c___p_r_e_f_i_x_}_/_l_i_b_/_p_y_t_h_o_n_<_v_e_r_s_i_o_n_>
              Recommended locations of the directories containing the standard modules.

       _$_{_p_r_e_f_i_x_}_/_i_n_c_l_u_d_e_/_p_y_t_h_o_n_<_v_e_r_s_i_o_n_>
       _$_{_e_x_e_c___p_r_e_f_i_x_}_/_i_n_c_l_u_d_e_/_p_y_t_h_o_n_<_v_e_r_s_i_o_n_>
              Recommended locations of the directories containing the include files needed for developing Python extensions  and  embedding  the
              interpreter.

       _~_/_._p_y_t_h_o_n_r_c_._p_y
              User-specific initialization file loaded by the _u_s_e_r module; not used by default or by most applications.

EENNVVIIRROONNMMEENNTT VVAARRIIAABBLLEESS
       PYTHONHOME
              Change the location of the standard Python libraries.  By default, the libraries are searched in ${prefix}/lib/python<version> and
              ${exec_prefix}/lib/python<version>, where ${prefix} and ${exec_prefix} are installation-dependent directories, both defaulting  to
              _/_u_s_r_/_l_o_c_a_l.  When $PYTHONHOME is set to a single directory, its value replaces both ${prefix} and ${exec_prefix}.  To specify dif‐
              ferent values for these, set $PYTHONHOME to ${prefix}:${exec_prefix}.

       PYTHONPATH
              Augments the default search path for module files.  The format is the same as the shell's $PATH: one or more  directory  pathnames
              separated  by colons.  Non-existent directories are silently ignored.  The default search path is installation dependent, but gen‐
              erally begins with ${prefix}/lib/python<version> (see PYTHONHOME above).  The default search path is always appended  to  $PYTHON‐
              PATH.   If  a  script argument is given, the directory containing the script is inserted in the path in front of $PYTHONPATH.  The
              search path can be manipulated from within a Python program as the variable _s_y_s_._p_a_t_h.

       PYTHONSTARTUP
              If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in  in‐
              teractive  mode.   The  file is executed in the same name space where interactive commands are executed so that objects defined or
              imported in it can be used without qualification in the interactive session.  You can also change the prompts _s_y_s_._p_s_1 and  _s_y_s_._p_s_2
              in this file.

       PYTHONY2K
              Set  this to a non-empty string to cause the _t_i_m_e module to require dates specified as strings to include 4-digit years, otherwise
              2-digit years are converted based on rules described in the _t_i_m_e module documentation.

       PYTHONOPTIMIZE
              If this is set to a non-empty string it is equivalent to specifying the --OO option. If set to an integer, it is equivalent to spec‐
              ifying --OO multiple times.

       PYTHONDEBUG
              If this is set to a non-empty string it is equivalent to specifying the --dd option. If set to an integer, it is equivalent to spec‐
              ifying --dd multiple times.

       PYTHONDONTWRITEBYTECODE
              If this is set to a non-empty string it is equivalent to specifying the --BB option (don't try to write _._p_y_[_c_o_] files).

       PYTHONINSPECT
              If this is set to a non-empty string it is equivalent to specifying the --ii option.

       PYTHONIOENCODING
              If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr,  in  the  syntax  _e_n_c_o_d_i_n_g_‐
              _n_a_m_e::_e_r_r_o_r_h_a_n_d_l_e_r The _e_r_r_o_r_h_a_n_d_l_e_r part is optional and has the same meaning as in str.encode. For stderr, the _e_r_r_o_r_h_a_n_d_l_e_r
               part is ignored; the handler will always be ´backslashreplace´.

       PYTHONNOUSERSITE
              If this is set to a non-empty string it is equivalent to specifying the --ss option (Don't add the user site directory to sys.path).

       PYTHONUNBUFFERED
              If this is set to a non-empty string it is equivalent to specifying the --uu option.

       PYTHONVERBOSE
              If this is set to a non-empty string it is equivalent to specifying the --vv option. If set to an integer, it is equivalent to spec‐
              ifying --vv multiple times.

       PYTHONWARNINGS
              If this is set to a comma-separated string it is equivalent to specifying the --WW option for each separate value.

       PYTHONHASHSEED
              If this variable is set to "random", the effect is the same as specifying the --RR option: a random value is used to seed the hashes
              of str, bytes and datetime objects.

              If  PYTHONHASHSEED  is  set  to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the
              hash randomization.  Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to  allow  a
              cluster of python processes to share hash values.

              The  integer  must  be  a decimal number in the range [0,4294967295].  Specifying the value 0 will lead to the same hash values as
              when hash randomization is disabled.

AAUUTTHHOORR
       The Python Software Foundation: https://www.python.org/psf/

IINNTTEERRNNEETT RREESSOOUURRCCEESS
       Main website:  https://www.python.org/
       Documentation:  file:///usr/share/doc/python2.7/html/index.html (python-doc package) or https://docs.python.org/2/
       Developer resources:  https://docs.python.org/devguide/
       Downloads:  https://www.python.org/downloads/
       Module repository:  https://pypi.python.org/
       Newsgroups:  comp.lang.python, comp.lang.python.announce

LLIICCEENNSSIINNGG
       Python is distributed under an Open Source license.  See the file "LICENSE" in the Python source distribution for information on terms  &
       conditions for accessing and otherwise using Python and for a DISCLAIMER OF ALL WARRANTIES.

                                                                                                                                       PYTHON(1)
