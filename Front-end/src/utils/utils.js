const utils = {
    makeToast (title, text, variant = null) {
        this.$bvToast.toast(text, {
            title: title,
            toaster: 'b-toaster-top-center',
            variant: variant,
            solid: true,
            append: true
        })
    }
}

export default utils