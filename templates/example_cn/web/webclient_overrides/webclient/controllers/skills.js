
if (typeof(require) != "undefined") {
    require("../controllers/muddery_skills.js");
}

/*
 * Derive from the base class.
 */
Skills = function(el) {
	MudderySkills.call(this, el);
}

Skills.prototype = prototype(MudderySkills.prototype);
Skills.prototype.constructor = Skills;

/*
 * Set skills' data.
 */
Skills.prototype.setSkills = function(skills) {
    this.clearElements("#skill_list");
    var template = $("#skill_list>.template");
    
    for (var i in skills) {
        var obj = skills[i];
        var item = this.cloneTemplate(template);

        item.find(".skill_name")
            .data("dbref", obj["dbref"])
        	.text(obj["name"]);
            
        if (obj["icon"]) {
            item.find(".img_icon").attr("src", settings.resource_url + obj["icon"]);
        	item.find(".skill_icon").show();
        }
        else {
        	item.find(".skill_icon").hide();
        }

        var mp = obj["passive"] ? "被动" : obj["mp"];
        item.find(".skill_mp").html(mp);
        
		var desc = $$.text2html.parseHtml(obj["desc"]);
        item.find(".skill_desc").html(desc);
	}

	var height = $(window).innerHeight() - $("#skills_wrapper").offset().top - 16;
	this.paginator.refresh(height);
}
