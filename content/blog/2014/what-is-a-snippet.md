Title: What is an about:home snippet?
Date: 2014-06-30
Category: mozilla
Slug: what-is-a-snippet
Author: Michael Kelly
Summary: Clarifying what an about:home snippet is.

I was reading Adam Lofting's post, [_The Power of Webmaker Landing Pages_][webmaker-landing], and it referred to something called "The Snippet", and linked to a post on fundraising.mozilla.org called [_What is the "snippet"?_][what-is-snippet].

The page the fundraising blog refers to is actually called [about:home](about:home); the icon and bit of text below the search bar is the "snippet". Every time you view about:home, a snippet is randomly chosen from a set of snippets and shown. Once every 24 hours, the set of snippets you might see is updated. Snippets can execute JavaScript code, which allows things like snippets that replace the Firefox logo or snippets that show videos.

To understand how about:home snippets really work, you have to understand the two main players: Firefox and the Snippets Service.

[webmaker-landing]: http://adamlofting.com/1139/the-power-of-webmaker-landing-pages/
[what-is-snippet]: https://fundraising.mozilla.org/what-is-the-snippet/

## Firefox Fetches Snippet Code

From Firefox's perspective, snippets are just one big chunk of HTML, CSS, and JavaScript that it injects into about:home when you view it. It fetches this code from the [Snippets Service][snippets-service], a web service running at [https://snippets.mozilla.com](https://snippets.mozilla.com).

Whenever you view about:home, Firefox checks to see if it has fetched snippet code within the last 24 hours. If it has, it loads the snippet code. If it hasn't, it makes a request and fetches the snippet code, and saves it. The URL used for this request is long and contains several pieces of info useful for deciding which snippets to send you. On one of my test copies of Firefox 30, about:home fetches snippets with this URL:

[https://snippets.mozilla.com/4/Firefox/30.0/20140605174243/Darwin_Universal-gcc3/en-US/release/Darwin%2013.2.0/default/default/](https://snippets.mozilla.com/4/Firefox/30.0/20140605174243/Darwin_Universal-gcc3/en-US/release/Darwin%2013.2.0/default/default/)

The most useful parts of the URL are the version (30.0), the locale (en-US), and the release channel (release). These let us do things like localize snippets for different locales or create snippets that promote new features to the release channels that already have them.

Once it has the snippet code, Firefox injects it into about:home. After that, Firefox is done; it has no idea that the snippet code may contain multiple snippets or that only one should be displayed. Instead, the snippet code that is injected contains its own logic for choosing a snippet to display.

[snippets-service]: https://wiki.mozilla.org/Websites/Snippets

## Snippets Show Themselves

The Snippets Service stores a large set of snippets and chooses which ones to send to you based on the URL shown above. For example, a snippet that is in French will be configured to be shown only to users with "fr" as their locale.

Along with the snippets themselves, the snippet code sent by the service contains JavaScript code that randomly chooses one of the included snippets and displays it. This code also performs a few other important functions, such as measuring impressions on snippets so that we can measure the conversion rate.

Because snippets can contain JavaScript, they aren't limited to showing an icon and text. In the past, we've run snippets that have:

- Swapped out the Firefox logo with another image
- Loaded a video player within the homepage
- [Blacked out the entire homepage in protest][sopa-protest]

[sopa-protest]: https://blog.mozilla.org/blog/2014/01/18/remembering-sopapipa/

## You Can Too!

An about:home snippet is a powerful way of reaching a huge number of people. If you're interested in running a snippet to spread the word about something, file a bug under the [Snippets :: Campaign Bugzilla component][campaign-bugzilla]. The snippets content team will review your request and determine if your snippet should be accepted.

Have any more questions about how snippets work? Let me know, I'm happy to answer them!

[campaign-bugzilla]: https://bugzilla.mozilla.org/enter_bug.cgi?product=Snippets&component=Campaign
