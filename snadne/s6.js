const fetch = require("node-fetch")
const { Parser } = require("htmlparser2");
const { DomHandler } = require("domhandler");
// const htmlparser = require("htmlparser")
const domutils = require("domutils")

const START = "http://i.protab.cz/static/ulohy/01f/ogzovdvhcehhwfxbffaavynwhzodydcvenxrprakshpnhotrnuirnuqxqbhmqnovlbggbmqkgwqzvdy.html"

// const URLREGEX = /<iframe src=".+\.html" style="width: 100%; height: 50vh;"><\/iframe>/g

/**
 * 
 * @param {Number} ms 
 * @returns 
 */
const wait = (ms) => {
	return new Promise((resolve) => {
		setTimeout(resolve, ms)
	})
}

async function getURL(url) {
	const data = await fetch(url).then(response => response.text())
	// let match = URLREGEX.exec(data)
	// await wait(1000)
	const handler = new DomHandler((error, dom) => {
		if (error) {
			// Handle error
		} else {
			// Parsing completed, do something
			const filtered = domutils.findAll((elem) => {
				if (elem.tagName === "iframe")
					return true
			}, dom, true)
			const a = filtered.map(f=> {
				if (f.attribs.src == "https://c.xkcd.com/random/comic/") return false
				return getURL(`http://i.protab.cz/static/ulohy/01f/${f.attribs.src}`)
			}).filter(i=>i)
			if (!a[0]) console.log(filtered[0].attribs.src)
			else console.log(data)
			// console.log(filtered)
			// if (filtered.attribs?.src) {
			// 	return
			// }
			// dom.forEach((node) => {
			// 	console.log(node.type)
			// 	if (node.type == "iframe") {
			// 		console.log("IFRAME", node)
			// 	}
			// })
		}
	});
	const parser = new Parser(handler);
	parser.write(data);
	parser.end();
	// const handler = htmlparser.DefaultHandler(function (error, dom) {
	// 	if (error) {
	// 		return console.error(error)
	// 	} else {
	// 		console.log(dom)
	// 	}
	// })
	// const parser = new htmlparser.Parser(handler)
	// parser.parseComplete(data)
	// if (match) {

	// 	match = match[0]
	// 	// is not null
	// 	console.log(match, `http://i.protab.cz/static/ulohy/01f/${match.slice(13, match.length-46)}`)
	// 	match = match.slice(13, match.length-46)
	// 	return getURL(`http://i.protab.cz/static/ulohy/01f/${match}`)
	// }
	// else {
	// 	return console.log(data)
	// }
}
getURL(START)