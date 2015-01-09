.. |br| raw:: html

    <br/>


Clean and Green
---------------

Pragmatic Architecture Patterns

| PyAtl — January 8, 2015
| @drocco007


Why?
----


slide
-----

you build systems


slide
-----

build

*understandable*

systems


slide
-----

build

understandable, *testable*

systems


slide
-----

build

understandable, testable, *maintainable*

systems


slide
-----

build new or **transform existing** systems

such that they are

*understandable, testable, maintainable*

How?
----


slide
-----

*Simple* is better than **complex**


The pitch
---------


slide
-----

| *Data* and *transforms* are easier
| to understand and maintain
| than **coupled procedures**


slide
-----

Most objects are **coupled procedures**


slide
-----

Methods **implicitly depend** on

mutable instance state


slide
-----

Methods are therefore

**coupled** to that state


slide
-----

and therefore to each other


slide
-----

instead…


slide
-----

Build systems around

**functional transforms**

of *simple values* and *data structures*


Objection!
----------


slide
-----

No one argues the

*high-level expressivity* & *convenient testability*

of **pure functions**



slide
-----

So what's the problem?


slide
-----

.. code-block:: python

    >>> objections = {'a'} | {'b'}


slide
-----

“That's a fine academic toy,

but it can't build **real** systems.”


slide
-----

(“real” generally being a euphemism

for “HTML-producing” ;)



slide
-----

“We can't afford to

**rewrite**

our *whole system*!”


slide
-----

These concerns are understandable,


slide
-----

but not *true*


Claim
-----


slide
-----

You don't *need* a full rewrite


slide
-----

(and you definitely **should not** attempt one)


slide
-----

You *can* build real systems this way


The pitch
---------


slide
-----

*Simple* is better than **complex**


slide
-----

Build systems around

**functional transforms**

of *simple values* and *data structures*


How?
----

slide
-----

Apply the Clean Architecture


slide
-----

.. image:: static/CleanArchitecture.jpg


slide
-----

| “In general, the *further in* you go,
| the **higher level** the software becomes.
| The *outer circles* are mechanisms.
| The *inner circles* are policies.”


slide
-----

| “The important thing is
| that *isolated, simple* data structures
| are passed across the boundaries.”


slide
-----

| “When any of the *external parts*
| of the system become **obsolete**, like
| the database, or the web framework,
| you can **replace** those obsolete
| elements with a minimum of fuss.”

— Uncle Bob Martin


How?
----


slide
-----

Apply the Clean Architecture


slide
-----

using


Pragmatic Architecture Patterns
-------------------------------


Pragmatic
---------


slide
-----

Tools you can apply to existing systems


slide
-----

Techniques for limiting the

*required change surface*


slide
-----

smaller change surface

↓

iterative incremental improvement


slide
-----

smaller change surface

↓

measurable progress


slide
-----

smaller change surface

↓

higher confidence & likelihood of success


Architecture
------------


slide
-----

Addresses the design of the entire system


slide
-----

Framework for assigning responsibilities


Patterns
--------


slide
-----

Generalized problem types and

solution approaches


slide
-----


slide
-----

The idea is simple


slide
-----

Build systems around

**functional transforms**

of *simple values* and *data structures*


slide
-----

(but it's not necessarily **easy**…)



slide
-----

Exhibit A


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        agreement = EndUserAgreement.get(id)

        if agreement.start_date <= date.today():
            return {'success': False, 'msg': '<already active msg>'}
        if EndUserAgreement.query.count() == 1:
            return {'success': False, 'msg': '<only agreement msg>'}

        # In order to ensure there are no gaps in agreements, …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            # If the deleted agreement was the first one, then we find…
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

        agreement.delete()
        return {'success': True}


slide
-----

Fetch the agreement to delete from the ORM

.. code-block:: python

    def delete(self, id):
        agreement = EndUserAgreement.get(id)

        #                                                              …


slide
-----

Check that it is not yet active

.. code-block:: python

    def delete(self, id):
        #                                                              …

        if agreement.start_date <= date.today():
            return {'success': False, 'msg': '<already active msg>'}

        #                                                              …

(and format a message back if it is)


slide
-----

and that it is not the only agreement

.. code-block:: python

    def delete(self, id):
        #                                                              …

        if EndUserAgreement.query.count() == 1:
            return {'success': False, 'msg': '<only agreement msg>'}

        #                                                              …


slide
-----

| Adjust either the previous or next
| agreement to cover any gap

.. code-block:: python

    def delete(self, id):
        #                                                              …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

slide
-----

Engage

.. code-block:: python

    def delete(self, id):
        #                                                              …

        agreement.delete()
        return {'success': True}


slide
-----

So what's the problem?


Q:
--


Q:
--

How would you test this?

slide
-----

How would you test

* 5–6 ORM calls
* ≥ 3 business rules
* ≥ 5 axes of responsibility


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        agreement = EndUserAgreement.get(id)

        if agreement.start_date <= date.today():
            return {'success': False, 'msg': '<already active msg>'}
        if EndUserAgreement.query.count() == 1:
            return {'success': False, 'msg': '<only agreement msg>'}

        # In order to ensure there are no gaps in agreements, …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            # If the deleted agreement was the first one, then we find…
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

        agreement.delete()
        return {'success': True}


Q:
--


Q:
--

How would you implement

**custom rules**

if a client asked?


Counterpoint
------------

How could we possibly convert

**delete()**

to a purely functional form?


slide
-----

(for Pete's sake, dan, even the *name* has state mutation in it!)


Pattern 1: FauxO
----------------

Functional core, imperative shell


slide
-----

Imperative shell:

**procedural “glue”**  that offers

an *OO interface* & *manages dependencies*


slide
-----

Functional core:

implements **all** the *decisions*


Key rule
--------

Never mix *decisions* and **dependencies**


slide
-----

*logic* goes only in the **functional core**


slide
-----

*dependencies* go only in the **imperative shell**


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        agreement = EndUserAgreement.get(id)

        if agreement.start_date <= date.today():
            return {'success': False, 'msg': '<already active msg>'}
        if EndUserAgreement.query.count() == 1:
            return {'success': False, 'msg': '<only agreement msg>'}

        # In order to ensure there are no gaps in agreements, …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            # If the deleted agreement was the first one, then we find…
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

        agreement.delete()
        return {'success': True}



slide
-----

becomes


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        success, msg = agreements.delete(id)
        return {'success': success, 'msg': msg}


slide
-----

Our HTTP endpoint now does its

*one job*


slide
-----

call routing


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        success, msg = agreements.delete(id)
        return {'success': success, 'msg': msg}


slide
-----

We've reduced its **responsibility surface** four fold


slide
-----

It no longer has to change with

| the Agreement model
| the persistence subsystem
| the removal rules
| the gap adjustment rules


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        success, msg = agreements.delete(id)
        return {'success': success, 'msg': msg}


slide
-----

``agreements`` is a *manager* object in the imperative shell


slide
-----

``agreements`` gathers all the dependencies: stateful objects, system settings, required libraries


slide
-----

What does it look like?


Step 1: ``is_removable()``
--------------------------

.. code-block:: python

    # agreements.py                                  (imperative shell)

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        removable, reason = is_removable(agreement, all_agreements)

        # date adjustments temporariliy elided…

        if removable:
            agreement.delete()

        return removable, reason


slide
-----

Notice the pivot


slide
-----

``agreement.delete()`` is a mutation applied to a persisted (dependent) object


slide
-----

whereas


slide
-----

``is_removable()`` is logic that can be applied to a simple data structure


slide
-----

Build systems around

**functional transforms**

of *simple values* and *data structures*


slide
-----

What do we mean by

*simple values* and *data structures*


slide
-----

* atomic types: ``str``, ``int``, …
* structs or records
* collections of same: ``list``, ``set``, ``dict``


slide
-----

Litmus test: ``is_removable()`` should work on a plain, non-ORM object


slide
-----

.. code-block:: python

    >>> from collections import namedtuple
    >>> Agreement = namedtuple('Agreement', 'start_date end_date')


slide
-----

.. code-block:: python

    # agreements_core.py                               (functional core)

    >>> def is_removable(agreement, all_agreements):
    ...     assert agreement and agreement in all_agreements
    ...
    ...     if agreement.start_date <= date.today():
    ...         return False, 'already_active'
    ...     elif len(all_agreements) <= 1:
    ...         return False, 'only_agreement'
    ...     else:
    ...         return True, None


slide
-----

.. code-block:: python

    >>> from datetime import date
    >>> only_agreement = Agreement(date.today(), None)
    >>> removable, status = is_removable(only_agreement, [only_agreement])
    >>> removable
    False


slide
-----

.. code-block:: python

    >>> really_planning_ahead = date(3025, 1, 1)
    >>> current_agreement = Agreement(date.today(), really_planning_ahead)
    >>> next_agreement = Agreement(really_planning_ahead, None)
    >>> removable, status = is_removable(next_agreement, [current_agreement,
    ...                                                   next_agreement])
    >>> removable
    True


slide
-----

But don't we still have decisions in the shell?


slide
-----

.. code-block:: python

    # agreements.py                                  (imperative shell)

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        removable, reason = is_removable(agreement, all_agreements)

        # date adjustments temporariliy elided…

        if removable:
            agreement.delete()

        return removable, reason


slide
-----

*Practicality* beats **purity**


slide
-----

I might just leave this


slide
-----

The *decision* was made in the core;

the shell is merely *acting on* that decision


slide
-----

However


slide
-----

That's a pretty fine distinction…


slide
-----

you can't always rationalize this way


slide
-----

which leads to


Pattern 2: Callbacks
--------------------

.. code-block:: python

    # agreements.py (step 2)                          (imperative shell)

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        removable, reason = is_removable(agreement, all_agreements,
                                         remove_callback=agreement.delete)

        # date adjustments temporariliy elided…

        return removable, reason


slide
-----

.. code-block:: python

    # agreements_core.py (step 2)                      (functional core)

    >>> def is_removable(agreement, all_agreements, remove_callback=None):
    ...     assert agreement and agreement in all_agreements
    ...
    ...     if agreement.start_date <= date.today():
    ...         return False, 'already_active'
    ...     elif len(all_agreements) <= 1:
    ...         return False, 'only_agreement'
    ...     else:
    ...         remove_callback() if remove_callback else None
    ...         return True, None


slide
-----

Callbacks can help bridge boundary gaps
between

**lower-level mechanisms** (web, db)

and higher level *policy layers*


slide
-----

*without* coupling policies to mechanisms


slide
-----

Callbacks are excellent for

**limiting**

the *required change surface*


slide
-----

Quick example: what exam types are available to a candidate?


slide
-----

.. code-block:: python

    def available_types(all_types, …, check_functions=()):
        # other checks…

        return [exam_type for exam_type in all_types
                if not any(fn(exam_type) for fn in check_functions)]

If any check function returns an error message, the type is unavalable
to the candidate.


slide
-----

Example check: organization credit hold

.. code-block:: python

    def registration_open(self, exam_type):
        organization = self.candidate.organization

        if organization.registration_blocked(self.candidate, exam_type):
            return 'registration_blocked_org_credit_hold'


slide
-----

When I did this particular refactor, I was working on

*applications*

*Organizations* are two subsystems away…


slide
-----

The check function callback allowed me to

**circumscribe**

how much I needed to change


slide
-----

“I will refactor *applications*, and no further”


slide
-----

``available_types()`` is still a *pure function*,

testable with **just data**


slide
-----

.. code-block:: python

    def test_exam_type_available_if_check_is_false():
        exam_type = object()
        check_function = lambda exam_type: None

        assert exam_type in \
            available_types([exam_type], check_functions=[check_function])

    def test_exam_type_not_available_if_check_is_true():
        exam_type = object()
        check_function = lambda exam_type: 'I_dont_think_so'

        assert exam_type not in \
            available_types([exam_type], check_functions=[check_function])


slide
-----

Callbacks are a *powerful tool*


slide
-----

but easy to **overuse**


slide
-----

Keep calm

and

apply judiciously


slide
-----


slide
-----

So where were we?


slide
-----

.. code-block:: python

    # agreements.py (step 2)                          (imperative shell)

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        removable, reason = is_removable(agreement, all_agreements,
                                         remove_callback=agreement.delete)

        # date adjustments temporariliy elided…

        return removable, reason


slide
-----

With the date adjustments

.. code-block:: python

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        removable, reason = is_removable(agreement, all_agreements,
                                         remove_callback=agreement.delete)

        # In order to ensure there are no gaps in agreements, …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            # If the deleted agreement was the first one, then we find…
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

        return removable, reason

slide
-----

Challenge: disentangle the mutation from the rules


slide
-----

Rules

* what should be updated
* how it should be updated


Pattern 3: Delegated value
--------------------------

Shell assigns a value computed by the core


slide
-----

.. code-block:: python

    # agreements.py (step 3)                          (imperative shell)

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        def on_remove():
            agreement.delete()
            adjust_dates(minimum_start_date=agreement.start_date)

        removable, reason = is_removable(agreement, all_agreements,
                                         remove_callback=on_remove)

        return removable, reason


slide
-----

.. code-block:: python

    # agreements.py (step 3)                          (imperative shell)

    def adjust_dates(minimum_start_date=None):
        all_agreements = EndUserAgreement.query.order_by('start_date')

        for agreement, start, end in mind_the_gap(all_agreements,
                                                  minimum_start_date):
            agreement.start_date = start
            agreement.end_date = end


slide
-----

Find ordered pairs of agreements with gaps between them…

.. code-block:: python

    def adjust_dates(minimum_start_date=None):
        all_agreements = EndUserAgreement.query.order_by('start_date')

        for agreement, start, end in mind_the_gap(all_agreements,
                                                  minimum_start_date):
            # …


slide
-----

| and for each,
| update its dates
| as indicated by the core

.. code-block:: python

    def adjust_dates(minimum_start_date=None):
        for agreement, start, end in …:
            agreement.start_date = start
            agreement.end_date = end


slide
-----

The core implements the rules

* which agreements need to be updated
* what the new dates should be


slide
-----

a little ``itertools`` help (from stdlib docs)

.. code-block:: python

    >>> from itertools import izip, tee
    >>> def pairwise(iterable):
    ...     "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    ...     a, b = tee(iterable)
    ...     next(b, None)
    ...     return izip(a, b)


slide
-----

.. code-block:: python

    # agreements_core.py (step 3)                      (functional core)

    >>> def mind_the_gap(sorted_agreements, minimum_start_date=None):
    ...     first = sorted_agreements[0]
    ...
    ...     if minimum_start_date and first.start_date > minimum_start_date:
    ...         yield first, minimum_start_date, first.end_date
    ...
    ...     for a, b in pairwise(sorted_agreements):
    ...         if a.end_date < b.start_date:
    ...             yield a, a.start_date, b.start_date


.. slide
.. -----

.. <tests here>


.. slide
.. -----

slide
-----

Stepping back


slide
-----

We started here


slide
-----

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        agreement = EndUserAgreement.get(id)

        if agreement.start_date <= date.today():
            return {'success': False, 'msg': '<already active msg>'}
        if EndUserAgreement.query.count() == 1:
            return {'success': False, 'msg': '<only agreement msg>'}

        # In order to ensure there are no gaps in agreements, …
        previous_agreement = self.get_previous(agreement.start_date, id)
        if previous_agreement:
            previous_agreement.end_date = agreement.end_date
        elif agreement.end_date:
            # If the deleted agreement was the first one, then we find…
            next_agreement = self.get_next(agreement.start_date, id)
            if next_agreement:
                next_agreement.start_date = agreement.start_date

        agreement.delete()
        return {'success': True}


slide
-----

mixed responsibilities

unclear rules

monolithic expression of intent


slide
-----

Practically untestable


slide
-----

Our functional core

.. code-block:: python

    >>> def is_removable(agreement, all_agreements, remove_callback=None):
    ...     assert agreement and agreement in all_agreements
    ...
    ...     if agreement.start_date <= date.today():
    ...         return False, 'already_active'
    ...     elif len(all_agreements) <= 1:
    ...         return False, 'only_agreement'
    ...     else:
    ...         remove_callback() if remove_callback else None
    ...         return True, None

slide
-----

Functional core (cont.)

.. code-block:: python

    >>> def mind_the_gap(sorted_agreements, minimum_start_date=None):
    ...     first = sorted_agreements[0]
    ...
    ...     if minimum_start_date and first.start_date > minimum_start_date:
    ...         yield first, minimum_start_date, first.end_date
    ...
    ...     for a, b in pairwise(sorted_agreements):
    ...         if a.end_date < b.start_date:
    ...             yield a, a.start_date, b.start_date


slide
-----

| Eminently readable
| because each function remains at a
| *single level of abstraction*


slide
-----

.. code-block:: python

    >>> def is_removable(agreement, all_agreements, remove_callback=None):
    ...     assert agreement and agreement in all_agreements
    ...
    ...     if agreement.start_date <= date.today():
    ...         return False, 'already_active'
    ...     elif len(all_agreements) <= 1:
    ...         return False, 'only_agreement'
    ...     else:
    ...         remove_callback() if remove_callback else None
    ...         return True, None

slide
-----

Easily testable using *simple data structures*


slide
-----

* no special setup
* test calls are symmetric with production calls


slide
-----

Clear assignment of responsibilities

* Core → logic
* Shell → dependencies
* Endpoint → dispatch


slide
-----

FauxO interface provides a

*familiar façade*

to the rest of the system


slide
-----

Our HTTP endpoint

.. code-block:: python

    @expose()
    @identity.require(identity.has_permission('agreement_delete'))
    def delete(self, id):
        success, msg = agreements.delete(id)
        return {'success': success, 'msg': msg}


slide
-----

Callbacks provide

*boundaries*,

limiting what we're required to touch


slide
-----

Callbacks allow the core to direct the shell…


slide
-----

*without* coupling the shell to it


slide
-----

Our imperative shell

.. code-block:: python

    def delete(assignment_id):
        agreement = EndUserAgreement.get(id)
        all_agreements = EndUserAgreement.query

        def on_remove():
            agreement.delete()
            adjust_dates(minimum_start_date=agreement.start_date)

        removable, reason = is_removable(agreement, all_agreements,
                                         remove_callback=on_remove)

        return removable, reason


slide
-----

Imperative shell (cont.)


.. code-block:: python

    def adjust_dates(minimum_start_date=None):
        all_agreements = EndUserAgreement.query.order_by('start_date')

        for agreement, start, end in mind_the_gap(all_agreements,
                                                  minimum_start_date):
            agreement.start_date = start
            agreement.end_date = end


slide
-----

This example is from a

*real system*

that serves

*real HTML*!


slide
-----

No ivory tower constructions here


slide
-----

Is it **easy**? Perhaps not…


slide
-----

Is it worth it?


Absolutely
----------


slide
-----

slide
-----

T.S. Eliot


slide
-----

    Immature poets imitate;


slide
-----

    Immature poets imitate;

    mature poets *steal*

    — T.S. Eliot


slide
-----

Special thanks to

Brandon Rhodes the Great

from whom I've stolen many ideas over the years


slide
-----

Thank you!


slide
-----

♥

@drocco007

.. raw:: html

    <!-- single quote: ’
    double quotes: x“”x
    em-dash: —
    vertical ellipsis: ⋮
    arrows: ←, ↑, →, ↓, ↔, ↕, ↖, ↗, ↘, ↙ -->
    <script>
        window.slide_transition_time = 200;
    </script>
    <script src="static/jquery-1.6.2.min.js"></script>
    <script src="static/jquery.url.min.js"></script>
    <script src="static/slides2.js"></script>
