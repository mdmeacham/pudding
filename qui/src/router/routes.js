const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/pocs", component: () => import("pages/IndexPage.vue") },
      {
        path: "/pocs/:id",
        name: "poc",
        component: () => import("pages/POC.vue"),
        props: (route) => {
          id: route.params.id;
        },
      },
      { path: "", redirect: { path: "/pocs" } },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
