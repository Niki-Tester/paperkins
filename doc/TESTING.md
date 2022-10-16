## **During Development Testing**
During the development process, manual testing was carried out in the following ways:-

1. Manually tested each element responsiveness and appearance by running the application from the terminal, and opening the development browser.

1. Published the page on Heroku and shared with peers for testing and for them to provide feedback.

### **Manual Testing:**
* During testing, I used four different browsers to ensure cross-compatibility. The desktop browsers used by myself were:

  1. Chrome
  1. Firefox  
  1. Edge
  1. Safari

- Using devtools to simulate different screen sizes/devices down to 280px in width, allowed me to test responsiveness. 
- Additionally I used an iPhone 11 with Safari / Chrome browser, and Samsung Galaxy S21 with the Chrome browser, for further testing.

### **Testing User Stories from User Experience (UX) Section**
* ### First Time Visitor Goals:
  * As a first time visitor, I want to easily understand the main purpose of the site.
    - When the user first visits the page, they are greeted with a hero image for a background, along with a tag line "Unique & Colourful Crafts" along with a call to action button, inviting the user to start shopping.

  * As a first time visitor, I want to be able to navigate the site to find content easily.
    - Responsive design is employed across all pages to deliver a satisfying UX on mobile, tablet, laptop and large desktop PC displays. Where the Nav elements are easily reachable regardless of screen size, with the elements collapsing into a menu for small screens

    - The navigation bar is displayed on all pages and is available regardless of the platform the user is using, providing the user with links where they will be able to register/login and view their cart.

    - The user is able to click on the menu in the navigation bar at any time, display a list of navigation links the user can use to navigate around the site..

  * As a first time visitor, I want to be able to browse through the available products.
    - When the user clicks on the "Shop Now" call to action button, the are immediately presented with the products page, allowing the user to browse the available products.

  * As a first time visitor, I want to be able to purchase something without having to create an account.
    - While the user is browsing the products page, they are able to select a product to view further details about the product.

    - The user can then add the product to the cart should they wish to purchase it.

    - Once added to the cart, the cart icon will be highlighted in blue.

    - Clicking on the cart the user is taken to view their full cart information. The user is presented with two options, to continue shopping or proceeding to a secure checkout. If the user is happy with all the items in their cart, clicking the secure checkout button will display the checkout page.

    - On the checkout page the user is presented with a form to complete their personal, delivery & payment information. Once the user has completed the form, and checked their order summary pressing the complete order button processes the users payment, and if the payment is successful, sends the user a confirmation email, and displays the final order confirmation to the user.

* ### Returning Visitor Goals:
  * As a returning visitor, I want to create an account.
    - Available from the navigation bar clicking the My Account dropdown a register link is displayed.

    - Once the register link is clicked, the user is immediately presented with a form where they can enter their email address, username, password & password confirmation.

    - Once the user completes the form clicking the Sign Up button triggers an email to be sent to the user where they must validate their email before signing in.

    - In the email, the user can click on the provided link, which redirects them to the email confirmation page, where the user will confirm the email address is to be associated with the provided username.

    - Once the user has completed this action, they are then able to successfully sign in.


  * As a returning visitor, I want to login to my account.
    - Available from the navigation bar clicking the My Account dropdown a log in link is displayed.

    - Once the log in link is clicked, the user is immediately presented with a form where they can enter their email address or username, password.

    - If the user provides valid credentials, and have validated their email from the registration step, the user will be immediately signed in.

  * As a returning visitor, I want to view my order history.
    - After the user has logged in, clicking the my account navigation drop down, the user is presented with a my profile link. 

    - Following this link the user will be immediately presented with their profile, displaying their order history.

  * As a returning visitor, I want to contact the seller with a general enquiry.
    - Clicking the Contact us link in the footer displays a modal to the user containing a form.

    - Completing this form successfully sends the user a confirmation email that their query has been received.

* ### Frequent Visitor Goals:
  * As a frequent visitor, I want to subscribe to a newsletter.
   - Successfully completing the newsletter form in the footer adds the users information to the database, and sends a confirmation email to the user.

  * As a frequent visitor, I want to change my account password.
   - Within the My Profile page a user will find the change password link.

   - Once clicked, the user is immediately presented with a form where they must enter their current password, along with their new password & confirm password.

   - Successfully completing this form immediately updates the users password, and a toast message is displayed to confirm the change was successful.

  * As a frequent visitor, I want to save my delivery information.
    - Within the My Profile page, the user is presented with a form where they can enter their default delivery information.

    - Once the form has been successfully completed the users default delivery information is saved in the database, and a toast message is displayed to confirm this.

  * As a returning visitor, I want to contact the seller with a delivery enquiry.
    - When the user makes a purchase, they are sent a confirmation email.

    - Within the confirmation email, an email address is provided to the user should they have any queries.

    - The user can also competed the Contact Us form, found in the footer should they have not received this email.

* ### Admin Goals:
  * As an Admin, I want to create a new category.
    - When the signed in user has admin permissions they are presented with additional links in the My Account dropdown.

    - Clicking the Admin Panel link will take the user to the Admin page for the site.

    - Here the user will be able to browse the current categories, and add a new category.

    - Once the category has been added, it is immediately added to the categories list in the database.

  * As an Admin, I want to add a new product.
    - When the signed in user has admin permissions they are presented with additional links in the My Account dropdown.

    - Clicking the Add Product link will take the user to the Add Product page.

    - The user is now presented with a form to complete, where entering all the required fields allows the user to add a new product.

    - The product is immediately saved in the database, and viewable on the products page.

  * As an Admin, I want to view a list of users subscribed to the newsletter.
    - When the signed in user has admin permissions they are presented with additional links in the My Account dropdown.

    - Clicking the Admin Panel link will take the user to the Admin page for the site.

    - Here the user will be able to navigate to the newsletter section, and will be presented with a list of users that have subscribed to the newsletter.

  * As an Admin, I want to respond to users query.
    - When the signed in user has admin permissions they are presented with additional links in the My Account dropdown.

    - Clicking the Customers Queries link will take the user to the Customer Queries page.

    - The user will immediately be presented with a list of all customer queries, separated by Outstanding/Completed queries. Clicking on an outstanding query, the user is presented with a text field.
    
    - Once the user has completed their response message, clicking the send button will immediately move the query into the Completed list, and send the customer an email with the response.

  * As an Admin, I want to remove a product.
    - When the signed in user has admin permissions, selecting a product from the products page to view its details, provides the user with a Delete button.

    - This button is highlighted in red to signify danger, and when clicked a confirmation modal is displayed with a warning message.

    - Once the user clicks to confirm they wish to delete a product, the product is immediately removed from the database, and if an image was linked to the product, the image is remove from media storage.

    - The user can also complete this action from the Admin Panel.


  * As an Admin, I want to update/change a product.
      - When the signed in user has admin permissions, selecting a product from the products page to view its details, provides the user with a Edit button.

    - This button is highlighted in blue, and when clicked the user is presented with the update product page. Where the products details are prefilled in a form for the user to edit.

    - Once the user has made the necessary changes and clicks the update product button, the product is immediately updated in the database, and if the image was changed, the old image is remove from media storage.

    - The user can also complete this action from the Admin Panel.

  * As an Admin, I want to view a list of orders.
      - When the signed in user has admin permissions they are presented with additional links in the My Account dropdown.

    - Clicking the Admin Panel link will take the user to the Admin page for the site.

    - Here the user will be able to navigate to the orders section, and will be presented with a list of orders that have been purchased by users.

### **Code Validation:**

The W3C Markup Validator, W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project, along with JsHint for validating all Javascript used, along with PEP8 for all Python code.

All validators passed without any errors.

---

[Return to README](/README.md)