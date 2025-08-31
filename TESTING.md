# TESTING

## 1. About Testing
The English Studio website has undergone extensive manual testing to ensure functionality, accessibility, and a smooth UX across devices. This document records **methods**, **steps**, and **results** for each area.

- Codebase validated where applicable (HTML/CSS), and forms & views tested end-to-end.
- The website owner was the primary manual tester recorded herin. Other informal manual testers were enlisted and provided feedback on their experience, their findings are not recorded. 
- privacy.html, 500.html, and 404.html are not included in the testing process. 
- A detailed bug/change log is maintained in **BUGLOG.md**.

---

## 2. Validation <a id="validation"></a>

### HTML (W3C HTML5)
**Method:** https://validator.w3.org/   
**Results:** 

| Page                    | Result                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| blog/blog_detail.html   | <img src="readmefiles\devicetesting\htmltesting\blog_detail.html.png" width="250" style="object-fit:contain;"/> |
| blog/blog_list.html     | <img src="readmefiles\devicetesting\htmltesting\blog_list.html.png" width="250" style="object-fit:contain;"/>   |
| blog/form.html          | <img src="readmefiles\devicetesting\htmltesting\form.html.png" width="250" style="object-fit:contain;"/>        |
| blog/list.html          | <img src="readmefiles\devicetesting\htmltesting\list.html.png" width="250" style="object-fit:contain;"/>        |
| contact.html            | <img src="readmefiles\devicetesting\htmltesting\contact.html.png" width="250" style="object-fit:contain;"/>     |
| flyers/flyer_form.html  | <img src="readmefiles\devicetesting\htmltesting\flyer_form.html.png" width="250" style="object-fit:contain;"/>  |
| flyers/flyers_list.html | <img src="readmefiles\devicetesting\htmltesting\flyers_list.html.png" width="250" style="object-fit:contain;"/> |
| flyers/reorder.html     | <img src="readmefiles\devicetesting\htmltesting\reorder.html.png" width="250" style="object-fit:contain;"/>     |
| index.html              | <img src="readmefiles\devicetesting\htmltesting\index.html.png" width="250" style="object-fit:contain;"/>       |
| portal/create_user.html | <img src="readmefiles\devicetesting\htmltesting\create_user.html.png" width="250" style="object-fit:contain;"/> |
| portal/dashboard.html   | <img src="readmefiles\devicetesting\htmltesting\dashboard.html.png" width="250" style="object-fit:contain;"/>   |
| portal/edit_user.html   | <img src="readmefiles\devicetesting\htmltesting\edit_user.html.png" width="250" style="object-fit:contain;"/>   |
| portal/login.html       | <img src="readmefiles\devicetesting\htmltesting\login.html.png" width="250" style="object-fit:contain;"/>       |
| portal/user_list.html   | <img src="readmefiles\devicetesting\htmltesting\user_list.html.png" width="250" style="object-fit:contain;"/>   |
| schedule/calendar.html  | <img src="readmefiles\devicetesting\htmltesting\calendar.html.png" width="250" style="object-fit:contain;"/>    |
| schedule/event_list.html| <img src="readmefiles\devicetesting\htmltesting\event_list.html.png" width="250" style="object-fit:contain;"/>  |

### CSS (W3C Jigsaw)
**Method:** https://jigsaw.w3.org/css-validator/  
**Scope:** All compiled CSS served in production (including any Bootstrap overrides).  
**Result:** 
CSS passed through the jigsaw validation checker with no errors. To better understand the purpose of each rule in the CSS file, refer to the comments which accompany every rule. 
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

### Links (W3C Link Checker)
**Method:** https://validator.w3.org/checklink  
**Result:** 
All links passed through the validator with the exception of 3 social links located in the footer (located at base.html) due to robots exclusion rules.

These 3 links were manually tested and validated:

https://www.linkedin.com/ - unpersonalised will update when client creates an account.

https://www.instagram.com/theenglishstudio.corvetto

https://www.facebook.com/ - unpersonalised will update when client creates business page.

### JavaScript Console
**Method:** JS was passed through JSHint.

**Results:** 
| Page                  | Screenshot                                                                                 | Notes |
|-----------------------|--------------------------------------------------------------------------------------------|-------|
| base.js      | <img src="readmefiles\devicetesting\jstesting\base.jpg" width="250"/>          |   PASS    |
| calendar.js    | <img src="readmefiles\devicetesting\jstesting\calendar.jpg" width="250"/>            |   PASS    |
| compress.js           | <img src="readmefiles\devicetesting\jstesting\compress.jpg" width="250"/>                 |   PASS    |
| contact.js           | <img src="readmefiles\devicetesting\jstesting\contact.jpg" width="250"/>                 |    PASS   |
| event.js        | <img src="readmefiles\devicetesting\jstesting\event.jpg" width="250"/>              |  PASS     |
| flyes.js     | <img src="readmefiles\devicetesting\jstesting\flyers.jpg" width="250"/>           |   PASS    |
| maps.js      | <img src="readmefiles\devicetesting\jstesting\maps.jpg" width="250"/>          |  PASS     |
| reorder.js         | <img src="readmefiles\devicetesting\jstesting\reorder.jpg" width="250"/>              |    PASS   |
| schedule.js        | <img src="readmefiles\devicetesting\jstesting\schedule.jpg" width="250"/>                |  PASS     |


Where feasible all inline JS is avoided. The only instances where inline JS is found is due to unavoidable Django variables ({% url %}, {{ csrf_token }}, {{ GOOGLE_MAPS_API_KEY }}), which must be rendered server-side. These stay as tiny inline config objects, for the external JS to consume.


### Accessibility (Lighthouse)
**Method:** Chrome DevTools → Lighthouse (Desktop & Mobile)  
**Record:** Accessibility & SEO  
**Result:** 
| Page                | Screenshot                                                                                   | Notes |
|---------------------|---------------------------------------------------------------------------------------------|-------|
| blog_detail.html    | ![blog_detail](readmefiles\devicetesting\lighthouse\blog_detail.jpg)                        |  PASS     |
| blog_list.html      | ![blog_list](readmefiles\devicetesting\lighthouse\blog_list.jpg)                            |    PASS   |
| contact.html        | ![contact](readmefiles\devicetesting\lighthouse\contact.jpg)                                |  PASS     |
| create_user.html    | ![create_user](readmefiles\devicetesting\lighthouse\create_user.jpg)                        |  PASS     |
| dashboard.html      | ![dashboard](readmefiles\devicetesting\lighthouse\dashboard.jpg)                            |   PASS    |
| edit_user.html      | ![edit_user](readmefiles\devicetesting\lighthouse\edit_user.jpg)                            |   PASS    |
| event_list.html     | ![event_list](readmefiles\devicetesting\lighthouse\event_list.jpg)                          |   PASS    |
| flyer_form.html     | ![flyer_form](readmefiles\devicetesting\lighthouse\flyer_form.jpg)                          |  PASS     |
| flyers_list.html    | ![flyers_list](readmefiles\devicetesting\lighthouse\flyers_list.jpg)                        |  PASS     |
| form.html           | ![form](readmefiles\devicetesting\lighthouse\form.jpg)                                      | PASS      |
| index.html          | ![index](readmefiles\devicetesting\lighthouse\index.jpg)                                    |   PASS    |
| list.html           | ![list](readmefiles\devicetesting\lighthouse\list.jpg)                                      |   PASS    |
| login.html          | ![login](readmefiles\devicetesting\lighthouse\login.jpg)                                    |   PASS    |
| schedule.html       | ![schedule](readmefiles\devicetesting\lighthouse\schedule.jpg)                              |    PASS   |
| user_list.html      | ![user_list](readmefiles\devicetesting\lighthouse\user_list.jpg)                            |  PASS     |

## 3. Mobile & Desktop Testing <a id="mobiletesting"></a>

The entire site was build on a widescreen desktop PC - for this reason only devices from phones upto laptop size screens are recorded in this testing document. The developer is adamant that the site is responsive to desktop sizing. Throughout the build DevTools has been used to test site wide responsivity across different viewport widths.

### Public pages testing table

| Page / Feature | iPhone 13 | Huawei P30 | iPad Pro 11 | Galaxy Tab S7 | Macbook Air | Notes |
|----------------|--------|--------|---------|------|-------|-------|
index.html | <img src="readmefiles/devicetesting/public/index.html/iPhone-13-PRO-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/iPhone-13-PRO-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/iPhone-13-PRO-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/iPhone-13-PRO-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/index.html/Huawei-P30-PRO-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/Huawei-P30-PRO-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/Huawei-P30-PRO-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/Huawei-P30-PRO-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\index.html\iPad-PRO-11-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\iPad-PRO-11-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\iPad-PRO-11-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/index.html/Galaxy-Tab-S7-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/Galaxy-Tab-S7-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles/devicetesting/public/index.html/Galaxy-Tab-S7-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | |
blog_list.html |<img src="readmefiles\devicetesting\public\blog\blog_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\blog\blog_list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\blog\blog_list.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\blog\blog_list.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\blog\blog_list.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/>| |
blog_detail.html | <img src="readmefiles/devicetesting/public/blog/blog_detail.html/iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/blog/blog_detail.html/Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/blog/blog_detail.html/iPad-PRO-11-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/blog/blog_detail.html/Galaxy-Tab-S7-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles/devicetesting/public/blog/blog_detail.html/Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | |
calendar.html | <img src="readmefiles\devicetesting\public\calendar.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\calendar.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\calendar.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\calendar.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\calendar.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\calendar.html\Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | |
contact.html | <img src="readmefiles\devicetesting\public\contact.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\contact.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\contact.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\contact.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\contact.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\contact.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\public\contact.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | |

### Staff pages testing table 

| Page / Feature | iPhone 13 | Huawei P30 | iPad Pro 11 | Galaxy Tab S7 | Macbook Air | Notes |
|----------------|-----------|------------|-------------|----------------|-------------|-------|
| portal/login.html | <img src="readmefiles\devicetesting\staff\portal\login.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\login.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\login.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\login.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\login.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> |  |
| portal/password_reset_form.html | <img src="readmefiles\devicetesting\staff\portal\password_reset_form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\password_reset_form.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\password_reset_form.html\iPad-PRO-11-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\password_reset_form.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\password_reset_form.html\Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> |  |
| portal/blog/confirm_delete.html | <img src="readmefiles\devicetesting\staff\portal\blog\confirm_delete.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\confirm_delete.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (10).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\confirm_delete.html\iPad-PRO-11-theenglishstudiocorvetto.com (9).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\confirm_delete.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (8).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\confirm_delete.html\Macbook-Air-theenglishstudiocorvetto.com (10).png" height="280" style="object-fit:contain;"/> |  |
| portal/blog/form.html | <img src="readmefiles\devicetesting\staff\portal\blog\form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\blog\form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\form.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (8).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\blog\form.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (9).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\form.html\iPad-PRO-11-theenglishstudiocorvetto.com (8).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\form.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (7).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\form.html\Macbook-Air-theenglishstudiocorvetto.com (9).png" height="280" style="object-fit:contain;"/> |  |
| portal/blog/list.html | <img src="readmefiles\devicetesting\staff\portal\blog\list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (7).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\list.html\iPad-PRO-11-theenglishstudiocorvetto.com (7).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\list.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\blog\list.html\Macbook-Air-theenglishstudiocorvetto.com (8).png" height="280" style="object-fit:contain;"/> |  |
| portal/flyers/flyer_form.html | <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\iPad-PRO-11-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> |  |
| portal/flyers/flyers_list.html | <img src="readmefiles\devicetesting\staff\portal\flyers\flyers_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyers_list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyers_list.html\iPad-PRO-11-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyers_list.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\flyers_list.html\Macbook-Air-theenglishstudiocorvetto.com (7).png" height="280" style="object-fit:contain;"/> |  |
| portal/flyers/reorder.html | <img src="readmefiles\devicetesting\staff\portal\flyers\reorder.html\iPhone-13-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\reorder.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\reorder.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\reorder.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\flyers\reorder.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> |  |
| portal/dashboard.html | <img src="readmefiles\devicetesting\staff\portal\dashboard.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\dashboard.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\dashboard.html\iPad-PRO-11-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\dashboard.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\dashboard.html\Macbook-Air-theenglishstudiocorvetto.com (7).png" height="280" style="object-fit:contain;"/> |  |
| portal/event_list.html | <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com.png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\event_list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPad-PRO-11-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPad-PRO-11-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\event_list.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> | <img src="readmefiles\devicetesting\staff\portal\event_list.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> |  |


### Browser Compatibility
| Page / Feature | Chrome | Safari | Firefox | Edge | Notes |
|----------------|--------|--------|---------|------|-------|
| Home (carousel, i18n flags) | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop PC |
| Blog list/detail | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop PC |
| Calendar (month nav, tooltips) | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop PC |
| Portal login/dashboard | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop PC |
| Portal blog/flyers/schedule forms | PASS | PASS | PASS | PASS | Browser tests conducted manually on windows desktop PC |

---

## 4. Manual Testing 

### Manual Testing Checklist 

### A. Internationalization (EN/IT)
| Step | Expected |  Result | Notes |
|-----|----------|--------|------|
| Click IT flag on Home | All content switches to Italian | PASS | All customer facing/public pages show full translations. Staff portal pages don't implement translations.  | 
| Switch EN→IT on Blog List & Detail | Titles/bodies follow locale | PASS | All customer facing/public pages show full translations. Staff portal pages don't implement translations.  | 
| Switch EN→IT on Calendar | Class names reflect chosen locale | PASS |All customer facing/public pages show full translations. Staff portal pages don't implement translations.   |

### B. Homepage (carousel, classes section, flyers feed)
| Step | Expected | Result | 
|-----|----------|--------|
| Carousel auto/arrow nav | Smooth transition, no console errors | PASS | 
| Class icons (AI icons) | Icons visible; labels readable | PASS | 
| Flyers order | Matches `sort_order` (portal) | PASS | | 

### C. Blog (public)
| Step | Expected | Result | 
|-----|----------|--------|
| Blog list shows cards | Title, image, date visible | PASS | 
| Card → detail | Slugged URL, content + media loads | PASS | 
| Prev/Next links | Navigate chronologically | PASS | 

### D. Schedule (public calendar)
| Step | Expected |  Pass | 
|-----|----------|--------|
| Month navigation | Previous/next months load | PASS | 
| Emoji per event | Emojis show in correct dates | PASS | 
| Tooltip on hover/tap | Shows one or multiple events for that date | PASS | 
| Recurrence display | Weekly/biweekly/monthly instances generated | PASS | 
| Exceptions | Skipped dates are **not** shown | PASS |  

### E. Contact + Newsletter + Map
| Step | Expected | Result |
|-----|----------|--------|
| Submit valid form | Success message; redirect with `?sent=1` | PASS | 
| Email delivery | Email received with correct `reply_to` | PASS | 
| Mailchimp opt-in checked | Subscriber added to list | PASS | 
| Mailchimp opt-in unchecked | No list entry created | PASS | 
| Invalid form | Errors shown; no submission | PASS | 
| Google Map loads | Custom pin visible; no console API errors | PASS | 

### F. Portal: Authentication & Security
| Step | Expected | Result | 
|-----|----------|--------|
| Visit `/portal/` logged out | Redirect to login | PASS |
| Login valid user | Dashboard visible | PASS |
| Logout | Session cleared; login required again | PASS |
| Password reset | Reset email flow works (templates render) | PASS |
| Direct access to portal sub-routes when logged out | Redirects to login | PASS |

### G. Portal: Blog CRUD
| Step | Expected | Result | 
|-----|----------|--------|
| Create blog post (EN/IT) | Saved; appears in list | PASS | 
| Upload image/video (Cloudinary) | Media previews; loads on detail | PASS |
| Edit / delete | Updates persist | PASS | _ |
| Draft vs Published | Draft hidden from public; Published visible | PASS | 

### H. Portal: Flyers CRUD & Reordering
| Step | Expected | Result | 
|-----|----------|--------|
| Create flyer (EN/IT) | Saved; can upload image/PDF | PASS |
| Toggle `publish` | Appears/disappears on Home | PASS |
| Change `sort_order` | Home list updates to new order | PASS |

### I. Portal: Classes & Events (Recurrence)
| Step | Expected | Result |
|-----|----------|--------|
| Create Class (EN/IT, emoji) | Visible in event form + calendar | PASS |
| Create Event (one-time) | Displays on selected date | PASS |
| Create Event (weekly/biweekly/monthly) | All instances appear correctly | PASS |
| Custom days (days_of_week) | Instances generated on chosen weekdays | PASS |
| Add Exceptions | Exception dates omitted | PASS |
| Edit/Delete event | Calendar updates accordingly | PASS |

### J. User Management (Django Auth)
| Step | Expected | Result | Notes |
|-----|----------|--------|------|
| Create user (staff) | Can log into portal | PASS | 
| Change permissions | Access reflects new roles | PASS |
| Delete user | Access revoked, can’t login | PASS | 

---

## 6. User Story Testing <a id="user"></a>

| User Story | Covered By |
|------------|------------|
| Teacher updates monthly schedule (recurrence & exceptions) | <img src="readmefiles\devicetesting\staff\portal\event_list.html\Macbook-Air-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\event_list.html\Macbook-Air-theenglishstudiocorvetto.com (6).png" height="280" style="object-fit:contain;"/> |
| Parent browses events with child | <img src="readmefiles\devicetesting\public\calendar.html\Galaxy-Tab-S7-theenglishstudiocorvetto.com (3).png" height="280" style="object-fit:contain;"/> |
| Owner manages posts/events/flyers in portal | <img src="readmefiles\devicetesting\staff\portal\event_list.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\flyers\flyer_form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\blog\form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\staff\portal\blog\form.html\iPhone-13-(iOS-15)-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> |
| Student finds IELTS/Business classes & contacts | <img src="readmefiles\devicetesting\public\index.html\iPad-PRO-11-theenglishstudiocorvetto.com (2).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\contact.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> |
| Sponsor/partner reviews professionalism | <img src="readmefiles\devicetesting\public\index.html\Macbook-Air-theenglishstudiocorvetto.com (1).png" height="280" style="object-fit:contain;"/> |
| Visitor selects contact category & subscribes | <img src="readmefiles\devicetesting\public\contact.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (4).png" height="280" style="object-fit:contain;"/> <img src="readmefiles\devicetesting\public\contact.html\Huawei-P30-PRO-theenglishstudiocorvetto.com (5).png" height="280" style="object-fit:contain;"/> |
| Newsletter subscriber receives updates | The website owner has not yet created a newsletter via MailChimp, so evidence is provided which illustrates that contact details are collected for future newsletters. <img src="readmefiles\mailchimp.png" height="280" style="object-fit:contain;"/> |



---

## 7. Known Issues & Bug Log
- See **BUGLOG.md** for a detailed overview of bugs which have been addressed throughout the project build.
- Outstanding issues (snapshot):  
  - 'collectstatic' leaves un-hashed duplicates (e.g., js/base.js) alongside hashed assets (e.g., js/base.43e960740ca8.js) inside the staticfiles folder. This has no impact at runtime because templates resolve hashed paths via {% static %} and WhiteNoise serves the manifest-fingerprinted files. This is simply a cosmetic mess in STATIC_ROOT which remains unresolved due to the project deadline. 
  - Semantics are often generalized throughout this project, primarily opting for 'div' - this issue does not relate to the project focus on database management and will therefore be handled post project deadline. The developer has a good understanding of semantics and intends to update the specificity across all templates from October 2025. 
  - CSS styling is not applied universally throughout the portal pages. Some styling improvements could be made to enhance the UX for the site owner. Styling contingency for the portal will be implemented post hand in from October 2025. 
  - All CRUD actions give feedback however in some instances there are duplicated in the form of a modal and a notification on the page. This is under the decision that it's better safe than sorry. It doesn't cause any real impact to the UX but this duplicate notification issue will be ironed out post hand in from October 2025. 
  - Italian translation feature is not implemented across the portal pages. Currently the only staff are native English speakers. All front end pages (customer facing) have been checked and ensure that translation is complete. The only exception to this is on the 'FOLLOW US' text in the footer. The translations will be implemented across the portal pages from October 2025. 


